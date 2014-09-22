# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///my_database.db', echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()

    print func.now()
    rs = session.execute(select([func.now()]))
    print rs.fetchone()
