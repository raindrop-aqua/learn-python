# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template, util
from google.appengine.ext import db
import json
import model
import os

class MainHandler(webapp.RequestHandler):
    def get(self):
        datas = model.modo_script.all().fetch(100, 0)
        data = [d.to_dict() for d in datas]
        json_string = json.dumps(data, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)

class PostHandler(webapp.RequestHandler):
    def get(self):
        post_page = os.path.join("assets", "post.html")
        self.response.out.write(template.render(post_page, {}))

    def post(self):
        self.response.content_type = "application/json"
        self.response.set_status(200)
        self.response.out.write("{'status':'ok!'}")

class AddHandler(webapp.RequestHandler):
    def get(self):
        import random
        json_string = '''
        {
            "name": "%s",
            "author": "渥美政廣",
            "url": "http://www.example.com/modo/assets/script.zip",
            "version": "%s",
            "rating": "%s",
            "description": "こんにちは\\nお元気ですか？"
        }
        '''
        name = "modo_script_%d" % random.randint(1, 1000)
        version = "1.0"
        rating = str(db.Rating(random.randint(0, 100)))
        jstr = json_string % (name, version, rating)

        obj = model.modo_script()
        json_obj = json.loads(jstr)

        obj.name = json_obj["name"]
        obj.author = json_obj["author"]
        obj.url = db.Link(json_obj["url"])
        obj.version = json_obj["version"]
        obj.rating = db.Rating(int(json_obj["rating"]))
        obj.description = json_obj["description"]
        obj.save()
        self.response.content_type = "text/plain"
        self.response.out.write('Add ok.')

application = webapp.WSGIApplication(
    [
        ("/", MainHandler),
        ("/post", PostHandler),
        ("/add", AddHandler)
    ],
    debug=True
)

def main():
    util.run_wsgi_app(application)

if __name__ == "__name__":
    main()
