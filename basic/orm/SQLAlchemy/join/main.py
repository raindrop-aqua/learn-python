# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, String, Integer, ForeignKey, MetaData
from sqlalchemy import select

metadata = MetaData()

news = Table('news', metadata,
             Column('id', Integer, primary_key=True),
             Column('title', String(80)),
             Column('body', String(250))
)

tag = Table('tag', metadata,
            Column('id', Integer, primary_key=True),
            Column('news_id', Integer, ForeignKey('news.id'))
)

print select(
    [news, tag]
).select_from(
    news.join(
        tag
    )
)




