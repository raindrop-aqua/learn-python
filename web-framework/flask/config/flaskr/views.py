# -*- coding: utf-8 -*-

from flaskr import app


@app.route('/')
def index():
    return app.config['SQLALCHEMY_DATABASE_URI']
