import webapp2
import os
import random
import jinja2
import datetime

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class DisplayHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/WelcomePage.html")
        self.response.write(start_template.render())

    #Verifies the user's age
    def post(self):
        user_age = self.request.get('Users-age')

        if user_age < 18:
            self.response.write("Sorry you cannot use our site")
        else:
            self.response.write("Welcome to our site we hope you enjoy")

class NumberInputHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/select.html")
        self.response.write(start_template.render())

    def post(self):
        number_template = jinja_current_dir.get_template("templates/displaynumbers.html")

        n1 = self.request.get('n1')
        n2 = self.request.get('n2')
        n3 = self.request.get('n3')
        n4 = self.request.get('n4')
        n5 = self.request.get('n5')
        n6 = self.request.get('n6')
        n7 = self.request.get('n7')

        numDict = {"n1":n1, "n2":n2, "n3":n3, "n4":n4, "n5":n5, "n6":n6, "n7":n7}
        self.response.write(number_template.render(numDict))

class WinningNumberHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/select.html")
        self.response.write(start_template.render())

    #def post(self):


app = webapp2.WSGIApplication([
('/', DisplayHandler),
('/numberInput', NumberInputHandler)
], debug=True)
