# -*- coding: utf-8 -*-

from insert import Person, Address, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my_database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

person = session.query(Person).first()
print person

address = session.query(Address).filter(Address.person == person).one()
print address


