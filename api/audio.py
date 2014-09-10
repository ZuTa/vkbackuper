import common

from models.audio import Audio, AudioAlbum


GET_AUDIO_COUNT = "audio.getCount"

def get_audio_count(access_token, user_id):
    url = common.create_method_url(GET_ALBUMS_COUNT, access_token, owner_id=)

    res = common.make_request(url)

    return int(res['response'])
