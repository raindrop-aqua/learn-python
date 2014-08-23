# coding: utf-8
from google.appengine.ext import db

class Data(db.Model):
    name = db.StringProperty(required=True, multiline=False)
    message = db.StringProperty(multiline=True)
    time = db.DateTimeProperty(auto_now_add=True)
