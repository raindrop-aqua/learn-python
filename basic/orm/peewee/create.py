# -*- coding: utf-8 -*-

from peewee import *
import datetime


db = SqliteDatabase('my_database.db', threadlocals=True)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datatime.now)
    is_published = BooleanField(default=True)
