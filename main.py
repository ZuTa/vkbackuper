import os, bottle, logging
import simplejson as json

from utils import common
from vkapi import auth, users, photos, audio
from gdapi import gdauth, drive


ARCHIVES_RELATIVE_PATH = "utils/archives"

REDIRECT_VK_URI = 'http://zuta.pythonanywhere.com/vk-login'
VK_AUTHORIZE_COOKIE = "vk-authorize"

GD_SCOPE = "https://www.googleapis.com/auth/drive"
GD_REDIRECT_URI = 'http://zuta.pythonanywhere.com/auth_return'
GD_AUTHORIZE_COOKIE = "gd-authorize"

vk_auth_url = None
vk_user = None

gd_flow = None
gd_service = None

def current_dir():
    return os.path.dirname(__file__)

@bottle.route('/')
@bottle.view('main')
def index():
    args = { "get_url" : application.get_url }

    return args

@bottle.route('/gd-authorize')
def gd_authorize():
    global gd_flow

    bottle.response.set_cookie(GD_AUTHORIZE_COOKIE, "", expires=0)

    gd_flow = gdauth.GDAuthorizationFlow(GD_SCOPE, GD_REDIRECT_URI)
    gd_flow.init()

    url = gd_flow.get_authorize_url()

    bottle.redirect(url)

@bottle.route('/auth_return')
@bottle.view('login')
def gd_auth_return():
    args = { "get_url" : application.get_url, "cookie_name" : GD_AUTHORIZE_COOKIE }

    result = False
    if bottle.request.query.code:
        global gd_service

        gd_credentials = gd_flow.get_credentials(bottle.request.query.code)

        gd_service = drive.DriveService(gd_credentials)
        gd_service.init()

        result = True

    bottle.response.set_cookie(GD_AUTHORIZE_COOKIE, "1" if result else "0")

    return args

@bottle.route('/vk-authorize')
def vk_authorize():
    bottle.response.set_cookie(VK_AUTHORIZE_COOKIE, "", expires=0)

    bottle.redirect(vk_auth_url)

@bottle.route('/vk-login')
@bottle.view('login')
def vk_login():
    args = { "get_url" : application.get_url, "cookie_name" : VK_AUTHORIZE_COOKIE}

    result = False
    if bottle.request.query.code:
        try:
            global vk_user
            vk_user = auth.login(bottle.request.query.code, REDIRECT_VK_URI)
            result = True
        except Exception:
            result = False

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

@bottle.route('/backup')
def backup():
    #TODO: check if user has completed all steps
    logging.info("start backuping")
    common.backup(gd_service, photos.get_all_photos(vk_user.access_token), audio.get_all_audio(vk_user.access_token))

@bottle.route('/static/:path#.+#', name='static')
def static(path):
    return bottle.static_file(path, root='static')


log_file_path = os.path.join(current_dir(), 'debug.log')

logging.basicConfig(format='%(asctime)s %(message)s',filename=log_file_path, filemode='w', level=logging.DEBUG)
logging.info(log_file_path)

auth.init()
vk_auth_url = auth.get_auth_url(REDIRECT_VK_URI)

application = bottle.default_app()
bottle.debug(True)
