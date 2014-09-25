# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, render_template, flash
from todo2apps import app, db
from todo2apps.models import Sentence


@app.route('/')
def index():
    sentence_list = Sentence.query.order_by(Sentence.create_at.desc()).all()
    return render_template('index.html', sentence_list=sentence_list)


@app.route('/add', methods=['POST'])
def add():
    sentence = Sentence(body=request.form['sentence'])
    db.session.add(sentence)
    db.session.commit()
    flash(u'TODOを追加しました。')
    return redirect(url_for('index'))


@app.route('/clear')
def clear():
    Sentence.query.delete()
    db.session.commit()
    flash(u'TODOをクリアしました。')
    return redirect(url_for('index'))
