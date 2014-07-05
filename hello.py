from bottle import route, run, template
import sys

#@route('/hello/<name>')
@route('/')
def index():
    return '<h1>Helo world!</h1>'
    #return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=sys.argv[1])
