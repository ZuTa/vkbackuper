class Photo(object):
    def __init__(self, _id, album_id, description, date, url):
        self._id = _id
        self._album_id = album_id
        self._description = description
        self._date = date
        self._url = url

    @property
    def album_id(self):
        return self._album_id

    @property
    def description(self):
        return self._description

    @property
    def date(self):
        return self._date

    @property
    def url(self):
        return self._url
