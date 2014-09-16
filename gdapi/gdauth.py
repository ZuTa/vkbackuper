import os

from oauth2client.client import flow_from_clientsecrets


CONFIG_FILE = 'config.json'

class GDAuthorizationFlow(object):

    def __init__(self, scope, redirect_uri, force=False):
        self._flow = None
        self._scope = scope
        self._redirect_uri = redirect_uri
        self._force = force

    def init(self):
        config_file_path = os.path.join(os.path.dirname(__file__), CONFIG_FILE)

        self._flow = flow_from_clientsecrets(config_file_path, ' '.join(self._scope))
        self._flow.redirect_uri = self._redirect_uri
        self._flow.approval_prompt = self._force

    def get_authorize_url(self):
        return self._flow.step1_get_authorize_url()

    def get_credentials(self, code):
        return self._flow.step2_exchange(code)