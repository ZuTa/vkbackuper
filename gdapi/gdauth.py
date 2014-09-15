import os
import simplejson as json

from oauth2client.client import OAuth2WebServerFlow


CONFIG_FILE = 'config.json'

class GDAuthorizationFlow(object):

    def __init__(self, scope, redirect_uri):
        self._flow = None
        self._scope = scope
        self._redirect_uri = redirect_uri

    def init(self):
        def get_config():
            current_dir = os.path.dirname(__file__)
            config_file_path = os.path.join(current_dir, CONFIG_FILE) 

            return json.loads(open(config_file_path, 'r').read())

        config = get_config()

        self.flow = OAuth2WebServerFlow(client_id=config['client_id'],
                                        client_secret=config['client_secret'],
                                        scope=self._scope,
                                        redirect_uri=self._redirect_uri)

    def get_authorize_url(self):
        return self.flow.step1_get_authorize_url()
