# -*- coding: utf-8 -*-
from google.appengine.ext import db
import utils

class BaseModel(db.Model):
    def to_dict(self):
        return utils.obj_to_dict(self)

class modo_script(BaseModel):
    name = db.StringProperty()
    author = db.StringProperty()
    url = db.LinkProperty()
    version = db.StringProperty(default = "0.0")
    rating = db.RatingProperty(default = 0)
    updated = db.DateTimeProperty(auto_now = True)
    description = db.StringProperty(multiline = True)
