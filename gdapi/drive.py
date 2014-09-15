import httplib2

from apiclient.discovery import build
from apiclient.http import MediaFileUpload


class DriveService(object):
    def __init__(self, credentials):
        self._credentials = credentials
        self._http = None

    def init(self):
        http = httplib2.Http()

        self._http = self._credentials.authorize(http)
        self._drive_service = build('drive', 'v2', http=http)

    def create_folder(self, folder_name):
        body = {
          'title': 'NEW FOLDER',
          'mimeType': 'application/vnd.google-apps.folder'
        }

        return self._drive_service.files().insert(body=body).execute()


    def upload_file(self, file_path):
        media_body = MediaFileUpload(file_path, mimetype='text/plain', resumable=True)
        body = {
          'title': 'ZUTA',
          'description': 'A test document',
          'mimeType': 'text/plain'
        }

        return self._drive_service.files().insert(body=body, media_body=media_body).execute()