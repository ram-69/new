from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')
        self.response.out.write("<br />")
        self.response.out.write('<img src="https://www.w3schools.com/tags/img_girl.jpg" alt="Girl in a jacket" width="500" height="600">                          ')
        self.response.out.write("<br />")
        self.response.out.write('#####################')

        even=[]
        odd=[]
        n=[]
        for i in range(100):
            if(i%2==0):
                even.append(i)
            else:
                odd.append(i)

        self.response.out.write(even)
        self.response.out.write(odd)
        ##################
        abc="anmol"
        nikhil=""

        for i in range(len(abc)):
            nikhil=nikhil+abc[i]

        print nikhil

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
