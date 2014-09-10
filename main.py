import os, bottle, logging

from utils.common import pack
from api import auth, users, photos
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

    return args

@bottle.route('/download-photos')
def download_photos():
    if is_session_new():
        bottle.redirect('/')

    user = get_user()

    logging.info('Start retrieving info about photos for user with {} id'.format( user.user_id))
    all_photos = photos.get_all_photos(user.access_token)
    logging.info('End retrieving info about photos for user with {} id'.format(  user.user_id))
    return all_photos[100].album.title
    name_to_url = zip(xrange(len(all_photos)), [photo.url for photo in all_photos])

    logging.info('Downloading and packing photos for user with {} id'.format(  user.user_id))
    arc = pack(name_to_url)
    logging.info('Done for user with {} id'.format(  user.user_id))

    bottle.redirect('/archive/{}'.format(arc))

@bottle.route('/archive/<arcname>')
def download_archive(arcname):
    return bottle.static_file(arcname, root=archive_path)


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

application = SessionMiddleware(bottle.default_app(), session_opts)
bottle.debug(True)
