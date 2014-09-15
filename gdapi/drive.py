import httplib2

from apiclient.discovery import build


class Drive(object):
    def __init__(self, credentials):
        self._credentials = credentials
        self._http = None

    def init(self):
        http = httplib2.Http()

        self._http = credentials.authorize(http)
        self._drive_service = build('drive', 'v2', http=http)
