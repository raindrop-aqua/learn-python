# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, DateTime, String, func
from todo2apps import db


class Sentence(db.Model):
    __tablename__ = 'sentence'
    id = Column(Integer, primary_key=True)
    body = Column(String(250))
    create_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return '%s: %s %s' % (self.id, self.create_at, self.body)


def init_db():
    db.create_all()


if __name__ == '__main__':
    init_db()
