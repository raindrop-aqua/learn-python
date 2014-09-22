# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, DateTime, String, func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Sentence(Base):
    __tablename__ = "sentence"
    id = Column(Integer, primary_key=True)
    body = Column(String(250))
    created_at = Column(DateTime, default=func.now())


def execute():
    engine = create_engine('sqlite:///my_database.db', echo=True)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    execute()