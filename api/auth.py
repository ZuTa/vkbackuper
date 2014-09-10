import json
import common

from models.users import User


CONFIG_FILE = 'config.json'
OAUTH_URL_PATTERN = 'https://oauth.vk.com/authorize?client_id={0}&scope=photos&redirect_uri={1}&response_type=code&v={2}'
TOKEN_URL_PATTERN = 'https://oauth.vk.com/access_token?client_id={0}&client_secret={1}&code={2}&redirect_uri={3}'

config = None

# decorator
def config_required(f):
    def wrapped(*args):
        if not config:
            raise Exception('Not configured')

        return f(*args)

    return wrapped


class Config(object):
    def __init__(self, app_id, app_secret, api_version):
        self._app_id = app_id
        self._app_secret = app_secret
        self._api_version = api_version

    @property
    def app_id(self):
        return self._app_id

    @property
    def app_secret(self):
        return self._app_secret

    @property
    def api_version(self):
        return self._api_version

    @staticmethod
    def parse(f):
        parsed = json.loads(open(f, 'r').read())

        return Config(parsed['APP_ID'], parsed['APP_SECRET'], parsed['API_VERSION'])


def init():
    global config

    if config:
        return

    import os

    current_dir = os.path.dirname(__file__)
    config_file_path = os.path.join(current_dir, CONFIG_FILE)

    config = Config.parse(config_file_path)

    common.update_api_version(config.api_version)

@config_required
def get_auth_url(redirect_uri):
    return OAUTH_URL_PATTERN.format(config.app_id, redirect_uri, config.api_version)

@config_required
def login(code, redirect_uri):
    parsed = common.make_request(TOKEN_URL_PATTERN.format(config.app_id, config.app_secret, code, redirect_uri))

    return User(parsed['access_token'], int(parsed['user_id']), int(parsed['expires_in']))
