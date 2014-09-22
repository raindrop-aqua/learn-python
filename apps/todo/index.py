# -*- coding: utf-8 -*-

from bottle import route, run, template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Sentence


@route('/')
def index():
    engine = create_engine('sqlite:///my_database.db', echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()

    sentence_list = session.query(Sentence).all()
    return template('index', sentence_list=sentence_list)


@route('/add', mothod='GET')
def add():
    sentence_body = request.query.sentence

    engine = create_engine('sqlite:///my_database.db', echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()

    sentence = Sentence(body=sentence_body)
    session.add(sentence)
    session.commit()

    return redirect('/')


@route('/clear')
def clear():
    engine = create_engine('sqlite:///my_database.db', echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()

    for sentence in session.query(Sentence).all():
        session.delete(sentence)
    session.commit()

    return redirect('/')


run(host='localhost', port=8000, debug=True, reloader=True)