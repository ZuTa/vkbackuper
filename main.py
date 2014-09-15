import os, bottle, logging
import simplejson as json

from utils import common
from api import auth, users, photos, audio
from models import photos as models_photos
from models import audio as models_audio


ARCHIVES_RELATIVE_PATH = "utils/archives"
REDIRECT_URI = 'http://zuta.pythonanywhere.com/login'
VK_AUTHORIZE_COOKIE = "vk-authorize"

auth_url = None
arhive_path = None

vk_user = None

def current_dir():
    return os.path.dirname(__file__)

@bottle.route('/')
@bottle.view('main')
def index():
    args = { "get_url" : application.get_url }

    return args

@bottle.route('/vk-authorize')
def vk_authorize():
    bottle.response.set_cookie(VK_AUTHORIZE_COOKIE, "", expires=0)

    bottle.redirect(auth_url)

@bottle.route('/login')
@bottle.view('login')
def login():
    args = { "get_url" : application.get_url }

    result = False
    if bottle.request.query.code:
        try:
            global vk_user
            vk_user = auth.login(bottle.request.query.code, REDIRECT_URI)
            result = True
        except Exception:
            result = False
    else:
        bottle.response.set_cookie(VK_AUTHORIZE_COOKIE, "0")
        return 'Something went wrong with authorization. Try again. (error:' + bottle.request.query.error + ' - ' + bottle.request.query.error_description + ')'

    bottle.response.set_cookie(VK_AUTHORIZE_COOKIE, "1" if result else "0")

    return args

@bottle.route('/vk-user')
def get_vk_user():
    if bottle.request.is_ajax:
        try:
            ui = users.get_user_info(vk_user.access_token)

            return json.dumps({"result" : "OK", "user":ui["user_name"]})
        except:
            #TODO: handle errors
            return json.dumps({"result" : "error"})

    return json.dumps({"result" : "error", "message" : "Only ajax requests allowed"});

@bottle.route('/welcome')
@bottle.view('welcome')
def welcome():
    args = users.get_user_info(user.access_token)

    args['photo_albums_count'] = photos.get_photo_albums_count(user.access_token)

    args['photos_count'] = photos.get_all_photos_count(user.access_token)

    args['audio_count'] = audio.get_audio_count(user.access_token, user.user_id)

    return args

@bottle.route('/pack-photos')
def pack_photos():
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

application = bottle.default_app()
bottle.debug(True)
