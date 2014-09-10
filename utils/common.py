import os, re, multiprocessing

from downloader import Downloader
from archivator import Archivator


DOWNLOADS_FOLDER = "downloads"
ARCHIVES_FOLDER = "archives"

pool = multiprocessing.Pool(processes=multiprocessing.cpu_count() * 2)
locker = multiprocessing.Lock()

def fetch_folder_path(path, locker):
    current_dir = os.path.dirname(__file__)
    downloads_path = os.path.join(current_dir, path)

    with locker:
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)

    return downloads_path

class Packer(object):
    def __init__(self, data, callback):
        self._data = data
        self._callback = callback



def pack(_data, callback):
    def inner(data, locker):
        downloads_folder = fetch_folder_path(DOWNLOADS_FOLDER, locker)
        archives_folder = fetch_folder_path(ARCHIVES_FOLDER, locker)

        downloader = Downloader(downloads_folder, data)
        if downloader.download():
            archivator = Archivator(downloader.destination, os.path.join(archives_folder, "{}.zip".format(downloader.uid)))
            archivator.archive()

        return os.path.basename(archivator.destination)

    async = pool.apply_async(inner, [_data, locker], callback=callback)

