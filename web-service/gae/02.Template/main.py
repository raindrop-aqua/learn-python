# coding: utf-8
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import sys
stdin = sys.stdin
stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdin = stdin
sys.stdout = stdout

class MainPage(webapp.RequestHandler):
    def get(self):
        params = {"message": "名前を入力してください。"}
        path = os.path.join(os.path.dirname(__file__), "views", "index.html")
        html = template.render(path, params)
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)

    def post(self):
        text1 = self.request.get("text1")
        params = {"message": "こんにちは、%sさん。" % text1}
        path = os.path.join(os.path.dirname(__file__), "views", "index.html")
        html = template.render(path, params)
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)


application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
