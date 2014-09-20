# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create import Base, Address, Person


def execute():
    engine = create_engine('sqlite:///basic/my_database.db', echo=True)
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()

    new_person = Person(name='john')
    session.add(new_person)
    session.commit()

    new_address = Address(post_code='5001001', person=new_person)
    session.add(new_address)
    session.commit()


if __name__ == '__main__':
    execute()


