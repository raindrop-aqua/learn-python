# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('todo2apps.config')

db = SQLAlchemy(app)

from todo2apps import views
