class AudioAlbum(object):
    def __init__(self, _id, title):
        self._id = _id
        self._title = title

    @property
    def title(self):
        return self._title
    

class Audio(object):
    def __init__(self, _id, artist, title, url, album_id):
        self._id = _id
        self._artist = artist
        self._title = title 
        self._url = url
        self._album_id = album_id
        
