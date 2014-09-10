class Album(object):
    def __init__(self, _id, title):
        self._id = _id
        self._title = title

    @property
    def uid(self):
        return self._id

    @property
    def title(self):
        return self._title


class Photo(object):
    def __init__(self, _id, album_id, description, date, url):
        self._id = _id
        self._album_id = album_id
        self._album = None
        self._description = description
        self._date = date
        self._url = url

    @property
    def album_id(self):
        return self._album_id

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, value):
        self._album = value

    @property
    def description(self):
        return self._description

    @property
    def date(self):
        return self._date

    @property
    def url(self):
        return self._url
