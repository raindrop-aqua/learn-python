# coding: utf-8

from google.appengine.ext import db

class ModoScript(db.Model):
    name = db.StringProperty()
    version = db.StringProperty()
    note = db.TextProperty()
    updated = db.DateTimeProperty(auto_now = True)

