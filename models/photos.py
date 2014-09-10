import os, re


def name_to_url(photos):
    """Returns list of tuples. Each tuple represents relation: extended name(album+photo) to photo's url
    """
    def replace_spaces(s):
        s = s.strip()
        return re.sub(r'\s+','_', s)

    result = []
    d = {}
    for photo in photos:
        album_title = replace_spaces(photo.album.title)
        album_id = photo.album_id
        if album_id not in d:
            d[album_id] = 0

        d[album_id] += 1
        result.append((os.path.join(album_title, '{}.jpg'.format(d[album_id])), photo.url))

    return result


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
