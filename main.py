import os, bottle, logging

from utils import common
from api import auth, users, photos, audio
from models import photos as models_photos
from models import audio as models_audio
from beaker.middleware import SessionMiddleware


ARCHIVES_RELATIVE_PATH = "utils/archives"
REDIRECT_URI = 'http://zuta.pythonanywhere.com/login'

auth_url = None
arhive_path = None

def current_dir():
    return os.path.dirname(__file__)

def is_session_new():
    session = bottle.request.environ.get('beaker.session')

    return session.get('user', None) is None

def get_user():
    session = bottle.request.environ.get('beaker.session')

    return session['user']

@bottle.route('/landing-page')
@bottle.view('landing_page')
def landing_page():
    args = { "get_url" : application.get_url }

    return args

@bottle.route('/')
def index():
    if is_session_new():
        bottle.redirect(auth_url)
    else:
        bottle.redirect('/welcome')

@bottle.route('/login')
def login():
    if not is_session_new():
        bottle.redirect('/welcome')

    if bottle.request.query.code:
        session = bottle.request.environ.get('beaker.session')
        session['user'] = auth.login(bottle.request.query.code, REDIRECT_URI)

        bottle.redirect('/welcome')
    else:
        return 'Something went wrong with authorization. Try again. (error:' + bottle.request.query.error + ' - ' + bottle.request.query.error_description + ')'

@bottle.route('/welcome')
@bottle.view('welcome')
def welcome():
    if is_session_new():
        bottle.redirect('/')

    user = get_user()

    args = users.get_user_info(user.access_token)

    args['photo_albums_count'] = photos.get_photo_albums_count(user.access_token)

    args['photos_count'] = photos.get_all_photos_count(user.access_token)

    args['audio_count'] = audio.get_audio_count(user.access_token, user.user_id)

    return args

@bottle.route('/pack-photos')
def pack_photos():
    if is_session_new():
        bottle.redirect('/')

    user = get_user()

    all_photos = photos.get_all_photos(user.access_token)

    name_to_url = models_photos.name_to_url(all_photos)

    arc = common.pack(name_to_url)

    return '/archive/{}'.format(arc)

@bottle.route('/pack-audio')
def pack_audio():
    if is_session_new():
        bottle.redirect('/')

    user = get_user()

    all_audio = audio.get_all_audio(user.access_token)

    name_to_url = models_audio.name_to_url(all_audio)

    arc = common.pack(name_to_url)

    return '/archive/{}'.format(arc)

@bottle.route('/archive/<arcname>')
def download_archive(arcname):
    return bottle.static_file(arcname, root=archive_path)

@bottle.route('/static/:path#.+#', name='static')
def static(path):
    return bottle.static_file(path, root='static')


log_file_path = os.path.join(current_dir(), 'debug.log')

logging.basicConfig(format='%(asctime)s %(message)s',filename=log_file_path, filemode='w', level=logging.DEBUG)
logging.info(log_file_path)

archive_path = os.path.join(current_dir(), ARCHIVES_RELATIVE_PATH)

auth.init()
auth_url = auth.get_auth_url(REDIRECT_URI)

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 43200,
    'session.data_dir': './data',
    'session.auto': True
}

#application = SessionMiddleware(bottle.default_app(), session_opts)
application = bottle.default_app()
#bottle.debug(True)

bottle.run(app=application, reloader=True)
