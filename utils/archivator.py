import os
import zipfile
import sys


def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for f in files:
            rel = os.path.relpath(root, path)
            dest = os.path.join(rel, f)
            # force to unicode (as folders/files may have special chars)
            dest = unicode(dest, 'utf-8')

            zip.write(os.path.join(root, f), dest)

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
