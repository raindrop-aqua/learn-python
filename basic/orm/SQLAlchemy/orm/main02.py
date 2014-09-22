# -*- coding: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create import Employee


if __name__ == '__main__':
    engine = create_engine('sqlite:///my_database.db', echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()

    emp2 = Employee(name='Marry')
    print emp2.hired_on
    session.add(emp2)
    print emp2.hired_on
    session.commit()
    print emp2.hired_on
    session.delete(emp2)
    session.commit()
    print session.query(Employee).count()
