# coding: utf-8
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import model 

class MainPage(webapp.RequestHandler):
    def get(self):
        datas = model.Data.all().order("-time").fetch(10, 0)
        params = {"datas": datas,
                  "message": "項目を入力して送信してください。"}
        path = os.path.join(os.path.dirname(__file__), "views", "index.html") 
        html = template.render(path, params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)
    def post(self):
        function = self.request.get("function")
        if function == "input":
            name = self.request.get("name")
            message = self.request.get("message")
            obj = model.Data(name=name, message=message)
            obj.save()
            self.redirect("/")
        else:
            id_number = self.request.get("id")
            data = model.Data.get_by_id(long(id_number))
            params = {"datas": [data],
                      "message": "検索しました。"}
            path = os.path.join(os.path.dirname(__file__), "views", "index.html") 
            html = template.render(path, params)
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(html)
            
            


application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
