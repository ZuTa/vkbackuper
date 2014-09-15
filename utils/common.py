import os, time, logging

from downloader import Downloader


TEMP_FOLDER = "temp"

def fetch_folder_path(folder_path):
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, folder_path)

    if not os.path.exists(path):
        os.makedirs(path)

    return path

def replace_spaces(s):
    s = s.strip()
    return re.sub(r'\s+','_', s)

class Backuper(object):

    def __init__(self, drive_service, downloader):
        self._drive_service = drive_service
        self._downloader = downloader

    def backup(self, photos, audio_tracks):
        root_folder = self._drive_service.create_folder("VK BACKUP %s" % time.strftime("%d-%m-%Y %H:%M:%S"))

        self._backup_photos(root_folder, photos)

    def _backup_photos(root_folder, photos):        
        folders = {}
        counters = {}
        for photo in photos:
            album_title = replace_spaces(photo.album.title)

            album_id = photo.album_id
            if album_id not in counters:
                counters[album_id] = 0
                folders[album_id] = self._drive_service.create_folder(album_title)

            counters[album_id] += 1

            local_file = downloader.download(photo.url)

            self._drive_service.upload_file(local_file, folder=folders[album_id])


def backup(drive_service, photos, audio_tracks):
    temp_folder = fetch_folder_path(TEMP_FOLDER)

    downloader = Downloader(temp_folder)

    backuper = Backuper(drive_service, downloader)
    backuper.backup(photos[:5], audio_tracks)
