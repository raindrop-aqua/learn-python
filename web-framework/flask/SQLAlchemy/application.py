# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(200))

    def __repr__(self):
        return '%s: %s' % (self.name, self.email)


db.create_all()

new_user = User(name='john doe', email='john@example.com')
db.session.add(new_user)
db.session.commit()

for user in db.session.query(User).all():
    print user


