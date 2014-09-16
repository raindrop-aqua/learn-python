# -*- coding: utf-8 -*-

from bottle import route, run, template, request, static_file


@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='./static')


@route('/')
def title():
    return template('title')


@route('/show', method='GET')
def men():
    username = request.query.username
    favorite = request.query.favorite

    return template('show', name=username, favorite=favorite)

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True, reloader=True)
