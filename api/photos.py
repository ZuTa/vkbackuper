import common
import re

from models.photo import Photo
from datetime import datetime

MAX_PHOTOS_TO_RETURN = 200

def get_photo_albums_count(access_token):
    url = common.create_method_url('photos.getAlbumsCount', access_token)

    res = common.make_request(url)

    return res['response']

def get_all_photos_count(access_token):
    url = common.create_method_url('photos.getAll', access_token)

    res = common.make_method_request(url)

    return int(res['count'])

def parse_photos(items, callback):
    for item in items:
        max_size, url = 0, None
        for inner_item in item:
            m = re.match(r"photo_(\d+)", inner_item)
            if m:
                size = m.group(1)
                if size > max_size:
                    max_size = size
                    url = item[inner_item]

        callback(Photo(int(item['id']), int(item['album_id']), item['text'], datetime.fromtimestamp(float(item['date']) / 1e3), url))

def get_all_photos(access_token):
    result = []
    offset = 0
    while True:
        url = common.create_method_url('photos.getAll', access_token, count=MAX_PHOTOS_TO_RETURN, offset=offset)
        json = common.make_method_request(url)

        parse_photos(json['items'], result.append)

        offset += len(json['items'])
        if int(json['count']) - offset == 0:
            break

    return result
