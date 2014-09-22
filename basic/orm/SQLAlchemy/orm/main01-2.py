# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create import Department, Employee


if __name__ == '__main__':
    engine = create_engine('sqlite:///my_database.db', echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()

    d1 = Department(name='IT')
    emp1 = Employee(name='john', department=d1)
    emp2 = Employee(name='smith', department=d1)
    session.add(d1)
    session.add(emp1)
    session.add(emp2)
    session.commit()
    print "before delete"
    print session.query(Employee).count()
    print session.query(Department).count()
    session.delete(d1)
    session.commit()
    print "after delete"
    print session.query(Employee).count()
    print session.query(Department).count()
