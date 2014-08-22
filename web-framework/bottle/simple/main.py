# coding: utf-8
from bottle import route, run

@route('/hello')
def hello():
    return u'こんにちは！'

run(host='localhost', port='8000', debug=True)

