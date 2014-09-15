import os
import uuid
import urllib2
import shutil
import logging

class Downloader(object):
    def __init__(self, destination):
        self._destination = destination

    @property
    def destination(self):
        return self._destination

    def download(self, url):
        _id = uuid.uuid4()

        local_file = os.path.join(self._destination, str(_id))

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

        return local_file
