import os
import uuid
import urllib2
import shutil
import logging

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

        for file_path, url in self._data:
            local_file = os.path.join(self._destination, file_path)

            os.makedirs(os.path.dirname(local_file))

            resp = urllib2.urlopen(url)

            try:
                f = open(local_file, 'wb')
                block_size = 8192
                while True:
                    chunk = resp.read(block_size)
                    if not chunk:
                        break
                    f.write(chunk)
            except Exception as e:
                logging("Error while downloading url: ex = {}, url = {}".format(e, url))
            finally:
                f.flush()
                f.close()

        if not result:
            shutil.rmtree(self._destination)

        return result
