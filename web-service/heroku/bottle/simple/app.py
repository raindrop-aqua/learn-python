# coding: utf-8

from bottle import route, run
from sys import argv

@route('/')
def hello():
	return u'こんにちは！'

run(host='0.0.0.0', port=argv[1])
