
from turtle import *
from os import *
import traceback

chdir("C:\\Users\\Dell\\Desktop\\random codes\\Free Roam")

s = Screen()
s.delay(0)
s.bgcolor("black")

def Start():

    start.ht()
    
    s.bgcolor("green")
    print("G")

def StartRButton(x,y):

    start.shape("startbup.gif")
        
    ontimer(Start, 40)

class Button(Turtle):

    def __init__(self,xc,yc, def_name = None):
        self.xc = xc
        self.yc = yc
        
        Turtle.__init__(self)

        if def_name == None:
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
        self.defined_name = def_name

        self.gshape()
        self.speed(0)
        self.pu()
        self.goto(xc,yc)
    
    def CButton(self,x,y):
        global pshapename
        self.shape(pshapename)

    def gshape(self):
        global upshapename, pshapename
        upshapename = self.defined_name + "bup.gif"
        pshapename = self.defined_name + "bp.gif"
        s.register_shape(upshapename)
        s.register_shape(pshapename)
        self.shape(upshapename) # eddd31 is the hex of the yellow in the start

start = Button(0,0)


listen()

start.onclick(start.CButton, 1)
start.onrelease(StartRButton, 1)
mainloop()
