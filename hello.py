from bottle import route, run, template

#@route('/hello/<name>')
@route('/')
def index(name):
    return template('<h1>Helo world!</h1>')
    #return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
