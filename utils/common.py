import os

from downloader import Downloader
from archivator import Archivator


DOWNLOADS_FOLDER = "downloads"
ARCHIVES_FOLDER = "archives"

def fetch_folder_path(path):
    current_dir = os.path.dirname(__file__)
    downloads_path = os.path.join(current_dir, path)

    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)

    return downloads_path

def pack(data):
    downloads_folder = fetch_folder_path(DOWNLOADS_FOLDER)
    archives_folder = fetch_folder_path(ARCHIVES_FOLDER)

    downloader = Downloader(downloads_folder, data)
    if downloader.download():
        archivator = Archivator(downloader.destination, os.path.join(archives_folder, "{}.zip".format(downloader.uid)))
        archivator.archive()

    return os.path.basename(archivator.destination)
