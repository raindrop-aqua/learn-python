# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import logging as log
import model
import os

class SearchService(webapp.RequestHandler):
    def get(self):
        items = model.ModoScript.all().order("-updated").fetch(100, 0)
        params = {
            "items": items
        }
        path = os.path.join(os.path.dirname(__file__), "assets", "list.html")
        html = template.render(path, params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)


class DetailService(webapp.RequestHandler):
    def get(self):
        id = self.request.get("id")
        item = model.ModoScript.get_by_id(long(id))
        params = {
            "id": item.key().id(),
            "name": item.name,
            "note": item.note,
            "version": item.version,
            "updated": item.updated
        }
        path = os.path.join(os.path.dirname(__file__), "assets", "detail.html")
        html = template.render(path, params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)
        log.info("### Get! ###")

    def post(self):
        import random
        obj = model.ModoScript()
        obj.name = "modo_script_%d" % random.randint(1, 100)
        obj.version = "1.%d" % random.randint(1, 10)
        obj.note = u"あいうえお\nかきくけこ"
        obj.put()
        log.info("### Post! ###")
        self.redirect("/")

    def put(self):
        '''  not supported. '''
        log.info("### Put! ###")

        self.redirect("/")

    def delete(self):
        '''  not supported. '''
        id = self.request.get("id")
        item = model.ModoScript.get_by_id(long(id))
        db.delete(item)

        log.info("### Delete! ###")
        self.redirect("/")
