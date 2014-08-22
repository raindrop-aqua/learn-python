# coding: utf-8
from bottle import route, run

@route('/')
def index():
    response = {u'code': u'0001'}
    return response

run(host='localhost', port=8000, debug=True, reloader=True)