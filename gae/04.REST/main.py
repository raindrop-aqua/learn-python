# coding: utf-8

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import controller


def main():
    application = webapp.WSGIApplication([
        ('/', controller.SearchService),
        ('/detail/.*', controller.DetailService)
    ], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__name__':
    main()
