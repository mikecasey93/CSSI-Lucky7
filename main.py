import webapp2
import os
import random
import jinja2
import datetime
from database import seed_data
from app_models import Lottery



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

        numDict = {"n1":n1, "n2":n2, "n3":n3, "n4":n4, "n5":n5, "n6":n6}
        userList = []
        userList.append(n1)
        userList.append(n2)
        userList.append(n3)
        userList.append(n4)
        userList.append(n5)
        userList.append(n6)
        self.response.write(number_template.render(numDict))

class OptionHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/option.html")
        self.response.write(start_template.render())


class LoadPage(webapp2.RequestHandler):
    def get(self):
        seed_data()
        #t = the_jinja_env.get_template('/templates/loader.html')
        self.response.write("done")
    #def post(self):

class RandomHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/random.html")
        self.response.write(start_template.render())

    def post(self):
        winningNumber = []
        newList = []
        userList = []
        for i in range(1,60):
            winningNumber.append(i)

        for j in range(1,7):
            index = random.randint(0,len(winningNumber)-1)
            newList.append(winningNumber[index])
            winningNumber.pop(index)

        winNumDict = {"wn1":newList[0], "wn2":newList[1], "wn3":newList[2], "wn4":newList[3], "wn5":newList[4], "wn6":newList[5]}
        start_template = jinja_current_dir.get_template("templates/randomdisplay.html")
        

        
        n1 = self.request.get('n1')
        n2 = self.request.get('n2')
        n3 = self.request.get('n3')
        n4 = self.request.get('n4')
        n5 = self.request.get('n5')
        n6 = self.request.get('n6')

        """winNumDict["n1"]=n1
        winNumDict["n2"]=n2
        winNumDict["n3"]=n3
        winNumDict["n4"]=n4
        winNumDict["n5"]=n5
        winNumDict["n6"]=n6
        """
        numDict = {"n1":n1, "n2":n2, "n3":n3, "n4":n4, "n5":n5, "n6":n6}
        userList.append(n1)
        userList.append(n2)
        userList.append(n3)
        userList.append(n4)
        userList.append(n5)
        userList.append(n6)

       
        for k in range(0,len(newList)-1):
            if userList[k] == newList[k]:
                numberMatch+=1
        """ 
        newWinList = {}
        newWinList["nw1"] = n1
        newWinList["nw2"] = n2 
        newWinList["nw3"] = n3 
        newWinList["nw4"] = n4
        newWinList["nw5"] = n5
        newWinList["nw6"] = n6
        """
        for l in range(len(userList)):
            if userList[l] in winNumDict.values():
                userList[l] = (int(userList[l]),"cl","match")
            else:
               userList[l] = (userList[l],"cl","NoMatch")
        """
        e = {"wn1":winNumDict["wn1"], "wn2":winNumDict["wn2"], "wn3":winNumDict["wn3"], "wn4":winNumDict["wn4"],"wn5":winNumDict["wn5"], "wn6":winNumDict["wn6"], "newWinList":newWinList}
        """
       
        self.response.write(start_template.render(winNumDict, userList=userList))


class ChooseDateHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/chooseDate.html")
        self.response.write(start_template.render())


    def post(self):
        date = self.request.get('Date')
        wn = Lottery.query().filter(Lottery.date >= date).get()
        #wn = Lottery.query(Lottery.date >= date).order(Lottery.date).get()
        
        win={"n1":wn.n1, "n2":wn.n2, "n3":wn.n3, "n4":wn.n4, "n5":wn.n5, "n6":wn.n6,"date": wn.date}
        start_template = jinja_current_dir.get_template("templates/winningnumber.html")
        
        n1 = int(self.request.get('n1'))
        n2 = int(self.request.get('n2'))
        n3 = int(self.request.get('n3'))
        n4 = int(self.request.get('n4'))
        n5 = int(self.request.get('n5'))
        n6 = int(self.request.get('n6'))
        
        numDict = {"n1":n1, "n2":n2, "n3":n3, "n4":n4, "n5":n5, "n6":n6}
        
        for i in numDict:
            if numDict[i] in win.values():
                numDict[i] = (numDict[i],"cl","match")
            else:
                numDict[i] = (numDict[i],"cl","NoMatch")



        d = {"win":win, "numDict":numDict}
        
        """userList.append(n1)
        userList.append(n2)
        userList.append(n3)
        userList.append(n4)
        userList.append(n5)
        userList.append(n6)
        """
        
        if n1 != "" and\
        n2 != "" and\
        n3 != "" and\
        n4 != "" and\
        n5 != "" and\
        n6 != "":
        
            wm = Lottery(n1 = int(n1), n2 = int(n2), n3 = int(n3), n4 = int(n4), n5 = int(n5), n6 = int(n6), date = date)

            self.response.write(start_template.render(d))
        
            for key in numDict:
                self.response.write(numDict[key])
                

        
        start_template = jinja_current_dir.get_template("templates/error.html")
        self.response.write(start_template.render())
            
               
        


app = webapp2.WSGIApplication([
('/', DisplayHandler), # age
('/load',LoadPage),
('/numberInput', NumberInputHandler), # manual entry for 6 numbers and a date
('/random', RandomHandler), # radom gate with manual entry for 6 num
('/chooseDate', ChooseDateHandler),
('/option', OptionHandler)
], debug=True)
