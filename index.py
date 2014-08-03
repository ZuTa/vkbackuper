from bottle import default_app, route, redirect,run

APP_ID = '4488301'
AUTH_URL = 'https://oauth.vk.com/authorize?client_id=' + APP_ID + '&scope=4&redirect_uri=http://zuta.pythonanywhere.com/start&response_type=code&v=5.23'

@route('/')
def login():
    redirect(AUTH_URL)

@route('/start')
def start():
    return 'Hello, code = ' + request.query.code

application = default_app()

#run(host='localhost',port='8083')
