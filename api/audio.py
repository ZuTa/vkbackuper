import common

from models.audio import Audio, AudioAlbum


MAX_AUDIO_TO_RETURN = 100
GET_AUDIO_COUNT = "audio.getCount"
GET_AUDIO = "audio.get"
GET_ALBUMS= "audio.getAlbums"

def get_audio_count(access_token, user_id):
    url = common.create_method_url(GET_AUDIO_COUNT, access_token, owner_id=user_id)

    res = common.make_request(url)

    return int(res['response'])

def parse_audio(items, callback):
    for item in items:
        url = item['url'].replace(".vk.me/", ".vk.com/")

        album_id = item.get('album_id', 0)

        callback(Audio(int(item['id']), album_id, item['artist'], item['title'], url))

def retrieve_audio_albums(access_token):
    albums = {}
    offset = 0
    while True:
        url = common.create_method_url(GET_ALBUMS, access_token, count=MAX_AUDIO_TO_RETURN, offset=offset)
        json = common.make_method_request(url)

        items = json['items']
        for item in items:
            album = AudioAlbum(int(item['id']), str(item['title']))

            albums[album.uid] = album

        offset += len(json['items'])
        if int(json['count']) - offset == 0:
            break

    return albums

def get_all_audio(access_token):
    result = []
    offset = 0
    while True:
        url = common.create_method_url(GET_AUDIO, access_token, count=MAX_AUDIO_TO_RETURN, offset=offset)
        json = common.make_method_request(url)

        parse_audio(json['items'], result.append)

        offset += len(json['items'])
        if int(json['count']) - offset == 0:
            break

    albums = retrieve_audio_albums(access_token)

    # inject albums into audio objects
    for audio in result:
        if audio.album_id != 0:
            audio.album = albums[audio.album_id]

    return result[:10]
