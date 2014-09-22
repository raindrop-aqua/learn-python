# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask!'


@app.route('/hello/<name>')
def hello(name=None):
    return 'Hello %s' % name


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
