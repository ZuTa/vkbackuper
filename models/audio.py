import os

def name_to_url(audios):
    """Returns list of tuples. Each tuple represents relation: extended name(album+audio) to audio's url
    """

    result = []
    for audio in audios:
        album_title = None
        if audio.album:
            album_title = audio.album.title.strip()

        file_name = '{} - {}.mp3'.format(audio.artist.strip(), audio.title.strip())
        full_path = os.path.join(album_title, file_name) if album_title else file_name
        result.append((full_path, audio.url))

    return result

class AudioAlbum(object):
    def __init__(self, _id, title):
        self._id = _id
        self._title = title.encode('UTF-8')

    @property
    def title(self):
        return self._title

    @property
    def uid(self):
        return self._id


class Audio(object):
    def __init__(self, _id, album_id, artist, title, url):
        self._id = _id
        self._artist = artist.encode('UTF-8')
        self._title = title.encode('UTF-8')
        self._url = url
        self._album_id = album_id
        self._album = None

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
    def url(self):
        return self._url

    @property
    def artist(self):
        return self._artist

    @property
    def title(self):
        return self._title