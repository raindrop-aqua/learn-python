# -*- coding: utf-8 -*-

from insert import Person, Address, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///basic/my_database.db', echo=True)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    person = session.query(Person).first()
    print person

    address = session.query(Address).filter(Address.person == person).one()
    print address


