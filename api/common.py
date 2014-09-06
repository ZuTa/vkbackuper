from urllib2 import urlopen


METHOD_URL = 'https://api.vk.com/method/'

api_version = '5.24'

def update_api_version(new_api_version):
    global api_version

    api_version = new_api_version

def make_request(url):
    response = urlopen(url)

    return json.loads(response.read())

def make_method_request(url):
    parsed = make_request(url)

    # TODO: handle errors

    # assume that all errors are handled
    return parsed['response']

def create_method_url(method_name, access_token=None, **params):
    params['v'] = api_version

    if access_token:
        params["access_token"] = access_token

    p = '&'.join([str(item) + '=' + str(params[item]) for item in params])

    url = METHOD_URL + method_name

    if len(p) > 0:
        url += '?' + p

    return url
