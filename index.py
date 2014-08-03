from bottle import route, run, template


@route('/')
def main():
    return '<h1> Hello, Victoria </h1>'

run(host='localhost', port=8082)
