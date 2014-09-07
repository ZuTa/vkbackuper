import os
import uuid
import urllib
import shutil


class Downloader(object):
    def __init__(self, destination, data):
        self._id = uuid.uuid4()
        self._data = data
        self._destination = os.path.join(destination, str(self._id))

    @property
    def uid(self):
        return str(self._id)

    @property
    def destination(self):
        return self._destination

    def download(self):
        result = True

        os.makedirs(self._destination)

        try:
            for file_name, url in self._data:
                urllib.urlretrieve(url, os.path.join(self._destination, "{}.jpg".format(file_name)))
        except:
            result = False

        if not result:
            shutil.rmtree(self._destination)

        return result
