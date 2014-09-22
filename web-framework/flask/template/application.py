# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'access to /hello/<name>'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

app.run(host='localhost', port=8000, debug=True)

