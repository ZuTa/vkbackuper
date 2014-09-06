import bottle

from urllib2 import urlopen

import json

APP_ID = '4491095'
APP_SECRET = 'CebOc1bgVW27jkKiS4Eh' # hide it
REDIRECT_URI = 'http://zuta.pythonanywhere.com/login'
API_VERSION = '5.24'
AUTH_URL = 'https://oauth.vk.com/authorize?client_id=' + APP_ID + '&scope=photos&redirect_uri=' + REDIRECT_URI + '&response_type=code&v=' + API_VERSION

METHOD_URL = 'https://api.vk.com/method/'

user = None

class User:
    def __init__(self, access_token, _id, expires_in):
        self.access_token = access_token
        self._id = _id
        self.expires_in = expires_in

    def token(self):
        return self.access_token

    def user_id(self):
        return self._id

def create_method_url(method_name, access_token=None, **params):
    params['v'] = API_VERSION

    if access_token:
        params["access_token"] = access_token

    p = '&'.join([str(item) + '=' + str(params[item]) for item in params])

    url = METHOD_URL + method_name

    if len(p) > 0:
        url += '?' + p

    return url

def make_request(url):
    response = urlopen(url)

    return json.loads(response.read())

def make_method_request(url):
    parsed = make_request(url)

    # TODO: handle errors

    # assume that all errors are handled
    return parsed['response']

@bottle.route('/')
def index():
    bottle.redirect(AUTH_URL)

@bottle.route('/login')
def login():
    if bottle.request.query.code:
        global user

        code = bottle.request.query.code

        parsed = make_request('https://oauth.vk.com/access_token?client_id=' + APP_ID + '&client_secret=' + APP_SECRET + '&code=' + code + '&redirect_uri=' + REDIRECT_URI)

        user = User(parsed['access_token'], int(parsed['user_id']), int(parsed['expires_in']))

        bottle.redirect('/welcome')
    else:
        return 'Something went wrong with authorization. Try again. (error:' + bottle.request.query.error + ' - ' + bottle.request.query.error_description + ')'


def get_user_info():
    url = create_method_url('users.get', user.token(), fields="photo_200")

    res = make_method_request(url)[0]

    user_name = res['first_name'] + ' ' + res['last_name']
    profile_photo_src = res['photo_200']

    return dict(user_name=user_name, profile_photo_src=profile_photo_src)

def get_photo_albums_count():
    url = create_method_url('photos.getAlbumsCount', user.token())

    res = make_request(url)

    return res['response']

def get_all_photos():
    url = create_method_url('photos.getAll', user.token(), photo_sizes=1)

    res = make_method_request(url)

    return dict(count=res['count'])


@bottle.route('/welcome')
@bottle.view('welcome')
def welcome():
    args = get_user_info()

    args['photo_albums_count'] = get_photo_albums_count()

    args['photos_count'] = get_all_photos()['count']

    return args


application = bottle.default_app()