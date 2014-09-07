import bottle
import bottle_session

from api import auth, users, photos

REDIRECT_URI = 'http://zuta.pythonanywhere.com/login'

user = None

@bottle.route('/')
def index():
    auth.init()

    url = auth.get_auth_url(REDIRECT_URI)

    bottle.redirect(url)

@bottle.route('/login')
def login():
    if bottle.request.query.code:
        global user

        user = auth.login(bottle.request.query.code, REDIRECT_URI)

        bottle.redirect('/welcome')
    else:
        return 'Something went wrong with authorization. Try again. (error:' + bottle.request.query.error + ' - ' + bottle.request.query.error_description + ')'

@bottle.route('/welcome')
@bottle.view('welcome')
def welcome():
    args = users.get_user_info(user.access_token)

    args['photo_albums_count'] = photos.get_photo_albums_count(user.access_token)

    args['photos_count'] = photos.get_all_photos_count(user.access_token)

    return args


application = bottle.default_app()

session_plugin = bottle_session.SessionPlugin(cookie_lifetime=10)

application.install(session_plugin)
