import common, re, logging

from models.photos import Photo, Album
from datetime import datetime


MAX_PHOTOS_TO_RETURN = 200
GET_ALBUMS_COUNT = 'photos.getAlbumsCount'
GET_ALL = 'photos.getAll'
GET_ALBUMS = 'photos.getAlbums'

def get_photo_albums_count(access_token):
    url = common.create_method_url(GET_ALBUMS_COUNT, access_token)

    res = common.make_request(url)

    return res['response']

def get_all_photos_count(access_token):
    url = common.create_method_url(GET_ALL, access_token)

    res = common.make_method_request(url)

    return int(res['count'])

def parse_photos(items, callback):
    for item in items:
        max_size, url = 0, None
        for inner_item in item:
            m = re.match(r"photo_(\d+)", inner_item)
            if m:
                size = int(m.group(1))
                if size > max_size:
                    max_size = size
                    url = item[inner_item]

        url = url.replace(".vk.me/", ".vk.com/")

        callback(Photo(int(item['id']), int(item['album_id']), item['text'], datetime.fromtimestamp(float(item['date']) / 1e3), url))

def retrieve_albums(access_token, album_ids):
    albums = dict.fromkeys(album_ids, None)

    url = common.create_method_url(GET_ALBUMS, access_token, album_ids=','.join(map(str, album_ids)))
    json = common.make_method_request(url)

    items = json['items']
    for item in items:
        album = Album(int(item['id']), item['title'])

        albums[album.uid] = album

    return albums

def get_all_photos(access_token):
    result = []
    offset = 0
    while True:
        url = common.create_method_url(GET_ALL, access_token, count=MAX_PHOTOS_TO_RETURN, offset=offset)
        json = common.make_method_request(url)

        parse_photos(json['items'], result.append)

        offset += len(json['items'])
        if int(json['count']) - offset == 0:
            break

    # retrieve albums
    album_ids = set([photo.album_id for photo in result])
    albums = retrieve_albums(access_token, album_ids)

    # inject albums into photo objects
    for photo in result:
        photo.album = albums[photo.album_id]

    return result
