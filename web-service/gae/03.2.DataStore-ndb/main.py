# coding: utf-8

import json
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import ndb

from model import Parent, Child


class ParentCreate(webapp.RequestHandler):
    def get(self):
        mail = self.request.get("mail")
        name = self.request.get("name")
        child_id = self.request.get("child_id")

        if child_id:
            child_key = ndb.Key(Child, child_id)
        else:
            child_key = None

        if mail:
            parent = Parent.get_by_id(mail)
            if parent:
                ret = {"status": "record already exists"}
            else:
                key = Parent(id=mail, parent_id=mail, name=name, child=child_key).put()
                parent = key.get()
                ret = parent.to_dict()
        else:
            ret = {"status": "no key"}

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ParentRead(webapp.RequestHandler):
    def get(self):
        mail = self.request.get("mail")

        if mail:
            parent = Parent.get_by_id(mail)
            if parent:
                ret = parent.to_dict()
            else:
                ret = {"status": "no record"}
        else:
            ret = {"status": "no key"}

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ParentUpdate(webapp.RequestHandler):
    def get(self):
        mail = self.request.get("mail")
        name = self.request.get("name")
        child_id = self.request.get("child_id")

        if child_id:
            child = Child.get_by_id(child_id)
        else:
            child = None

        if mail:
            parent = Parent.get_by_id(mail)
            if parent:
                parent.parent_id = mail
                parent.name = name
                if child_id:
                    parent.child = child
                parent.put()
                ret = parent.to_dict()
            else:
                ret = {"status": "no record"}
        else:
            ret = {"status": "no key"}

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ParentDelete(webapp.RequestHandler):
    def get(self):
        mail = self.request.get("mail")

        if mail:
            parent = Parent.get_by_id(mail)
            if parent:
                parent.key.delete()
                ret = {"status": "ok"}
            else:
                ret = {"status": "no record"}
        else:
            ret = {"status": "no key"}

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ParentList(webapp.RequestHandler):
    def get(self):
        mail = self.request.get("mail")
        name = self.request.get("name")

        ret = []

        if mail:
            parent = Parent.get_by_id(mail)
            if parent:
                ret.append(parent.to_dict())
        elif name:
            query = Parent.query(Parent.name == name)
            for p in query:
                ret.append(p.to_dict())
        else:
            query = Parent.query()
            for p in query:
                ret.append(p.to_dict())

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ChildCreate(webapp.RequestHandler):
    def get(self):
        child_id = self.request.get("child_id")
        name = self.request.get("name")

        if child_id:
            child = Child.get_by_id(child_id)
            if child:
                ret = {"status": "record already exists"}
            else:
                key = Child(id=child_id, child_id=child_id, name=name).put()
                child = key.get()
                ret = child.to_dict()
        else:
            ret = {"status": "no key"}

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ChildRead(webapp.RequestHandler):
    def get(self):
        child_id = self.request.get("child_id")

        if child_id:
            child = Child.get_by_id(child_id)
            if child:
                ret = child.to_dict()
            else:
                ret = {"status": "no record"}
        else:
            ret = {"status": "no key"}

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ChildUpdate(webapp.RequestHandler):
    def get(self):
        child_id = self.request.get("child_id")
        name = self.request.get("name")

        if child_id:
            child = Child.get_by_id(child_id)
            if child:
                child.child_id = child_id
                child.name = name
                child.put()
                ret = child.to_dict()
            else:
                ret = {"status": "no record"}
        else:
            ret = {"status": "no key"}

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ChildDelete(webapp.RequestHandler):
    def get(self):
        child_id = self.request.get("child_id")

        if child_id:
            child = Child.get_by_id(child_id)
            if child:
                child.key.delete()
                ret = {"status": "ok"}
            else:
                ret = {"status": "no record"}
        else:
            ret = {"status": "no key"}

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


class ChildList(webapp.RequestHandler):
    def get(self):
        child_id = self.request.get("child_id")
        name = self.request.get("name")

        ret = []

        if child_id:
            child = Child.get_by_id(child_id)
            if child:
                ret.append(child.to_dict())
        elif name:
            query = Child.query(Child.name == name)
            for c in query:
                ret.append(c.to_dict())
        else:
            query = Child.query()
            for c in query:
                ret.append(c.to_dict())

        json_string = json.dumps(ret, ensure_ascii=False)
        self.response.content_type = "application/json"
        self.response.out.write(json_string)


application = webapp.WSGIApplication(
    [
        ('/parent/create', ParentCreate),
        ('/parent/read', ParentRead),
        ('/parent/update', ParentUpdate),
        ('/parent/delete', ParentDelete),
        ('/parent', ParentList),
        ('/child/create', ChildCreate),
        ('/child/read', ChildRead),
        ('/child/update', ChildUpdate),
        ('/child/delete', ChildDelete),
        ('/child', ChildList)
    ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
