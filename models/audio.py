class AudioAlbum(object):
    def __init__(self, _id, title):
        self._id = _id
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def uid(self):
        return self._id


class Audio(object):
    def __init__(self, _id, album_id, artist, title, url):
        self._id = _id
        self._artist = artist
        self._title = title
        self._url = url
        self._album_id = album_id
        self._album = None

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, value):
        self._album = value
