import httplib2, logging

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

    def create_folder(self, folder_name, parent_id=None):
        logging.info("creating folder (parent = {})".format(parent_id))
        body = {
          'title': folder_name,
          'mimeType': 'application/vnd.google-apps.folder',
        }

        if parent_id:
            body["parents"] = [{"id" : parent_id}]
        logging.info(body);
        res = self._drive_service.files().insert(body=body).execute()
        logging.info(res);
        return res


    def upload_file(self, file_path, new_file_name, folder_id=None):
        logging.info("uploading file (folder = {})".format(folder_id))

        media_body = MediaFileUpload(file_path, mimetype='image/jpg', resumable=True)
        body = {
          'title': new_file_name,
        }

        if folder_id:
            body["parents"] = [{"id" : folder_id}]

        return self._drive_service.files().insert(body=body, media_body=media_body).execute()
