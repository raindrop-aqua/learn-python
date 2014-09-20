# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create import Base, Address, Person

engine = create_engine('sqlite:///my_database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_person = Person(name='john')
session.add(new_person)
session.commit()

new_address = Address(post_code='5001001', person=new_person)
session.add(new_address)
session.commit()

