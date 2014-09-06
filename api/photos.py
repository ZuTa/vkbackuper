import common


def get_photo_albums_count(access_token):
    url = common.create_method_url('photos.getAlbumsCount', access_token)

    res = common.make_request(url)

    return res['response']

def get_all_photos(access_token):
    url = common.create_method_url('photos.getAll', access_token, photo_sizes=1)

    res = common.make_method_request(url)

    return dict(count=res['count'])
