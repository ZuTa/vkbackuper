
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return '<h1>Hello from ZuTa and Victoria!</h1>'

application = default_app()

