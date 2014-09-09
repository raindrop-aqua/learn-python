# -*- coding: utf-8 -*-
from bottle import run, request, route


@route('/')
def index():
    print request

    json = {
        "HI": "10.5",
        "ZAITATE": "11.6",
        "SCTATE": "12.7",
    }
    return json


run(host="localhost", port=8000, debug=True, reloader=True)

