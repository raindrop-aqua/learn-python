from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import memcache


class MainPage(webapp.RequestHandler):
    def get(self):
        counter = incr_counter()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('counter: %d' % int(counter))

def incr_counter():
    data = memcache.get("counter")
    if data is not None:
        memcache.incr("counter")
        return data + 1
    else:
        memcache.set(key="counter", value=0, time=10)   # 10 sec
        return 0

def main():
    application = webapp.WSGIApplication(
        [('/', MainPage)],
        debug = True
    )
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

