# coding: utf-8
from google.appengine.ext import ndb
from google.appengine.api import memcache

class Child(ndb.Model):
    child_id = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=False)

class Parent(ndb.Model):
    parent_id = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    child = ndb.KeyProperty(kind=Child)

    def to_dict(self):
        ret = self._to_dict()
        child = Child.get_by_id(self.child.id())
        if child:
            ret["child"] = child.to_dict()
        else:
            ret["child"] = None
        return ret