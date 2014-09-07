import os
import zipfile
import sys

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for f in files:
            p = os.path.join(root, f)
            zip.write(p, os.path.basename(p))

class Archivator(object):
    def __init__(self, source, destination):
        self._source = source
        self._destination = destination

    @property
    def destination(self):
        return self._destination

    def archive(self):
        result = True

        try:
            zip_file = zipfile.ZipFile(self._destination, 'w')
            zipdir(self._source, zip_file)
            zip_file.close()
        except:
            sys.stderr.write('ERROR while archiving from {} to {}'.format(self._source, self._destination))
            sys.stderr.flush()
            result = False

        return result
