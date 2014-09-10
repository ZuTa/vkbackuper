import common
import re

from models.photos import Photo, Album
from datetime import datetime


MAX_PHOTOS_TO_RETURN = 200
GET_ALBUMS_COUNT = 'photos.getAlbumsCount'
GET_ALL = 'photos.getAll'

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

def get_all_photos(access_token):
    def inject_album(photo):
        # TODO: retrieve album
        url = common.create_method_url(GET_ALBUMS_COUNT, access_token, album_ids=photo.album_id)
        json = common.make_method_request(url)

        if int(json['count']) != 1:
            raise Exception('Cannot retrieve photo album with id = {}'.format(photo.album_id))

        parsed_album = json['items'][0]

        photo.album = Album(int(parsed_album['id']), parsed_album['title'])

        return photo

    result = []
    offset = 0
    while True:
        url = common.create_method_url(GET_ALL, access_token, count=MAX_PHOTOS_TO_RETURN, offset=offset)
        json = common.make_method_request(url)

        parse_photos(json['items'], lambda photo: result.append(inject_album(photo)))

        offset += len(json['items'])
        if int(json['count']) - offset == 0:
            break

    return result
