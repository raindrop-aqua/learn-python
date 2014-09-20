# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(30), nullable=False)

    def __repr__(self):
        return "%s: %s" % (self.id, self.name)


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street_name = Column('street_name', String(50))
    street_number = Column('street_number', String(50))
    post_code = Column('post_code', String(7), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def __repr__(self):
        return "%s: %s %s %s %s" % (
            self.id,
            self.street_name,
            self.street_number,
            self.post_code,
            self.person_id
        )

def execute():
    engine = create_engine('sqlite:///basic/my_database.db', echo=True)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    execute()
