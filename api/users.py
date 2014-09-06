def get_user_info(access_token):
    url = create_method_url('users.get', access_token, fields="photo_200")

    res = make_method_request(url)[0]

    user_name = res['first_name'] + ' ' + res['last_name']
    profile_photo_src = res['photo_200']

    return dict(user_name=user_name, profile_photo_src=profile_photo_src)
