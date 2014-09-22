# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create import Department, Employee


if __name__ == '__main__':
    engine = create_engine('sqlite:///my_database.db', echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()

    d = Department(name='IT')
    emp1 = Employee(name='john', department=d)
    session.add(d)
    session.add(emp1)
    session.commit()
    print "before delete"
    print session.query(Employee).all()
    print session.query(Department).count()
    session.delete(d)
    session.commit()
    print "after delete"
    print session.query(Employee).all()
    print session.query(Department).count()
