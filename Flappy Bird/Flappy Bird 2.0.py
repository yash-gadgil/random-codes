from turtle import *
from os import *
import traceback
import tkinter
from threading import Thread

info = tkinter.Tk()
screen_width = info.winfo_screenwidth()
screen_height = info.winfo_screenheight()
info.destroy()

files_path = getcwd()
chdir(files_path)

f_alive = True
falling = True

u = 3
t = 0

s = Screen()
s.title("Flappy Bird 2.0")
s.delay(0)

s.register_shape("background1.gif")
s.register_shape("flappyup.gif")
s.register_shape("flappydown.gif")

background = Turtle()
background.shape("background1.gif")

flappy = Turtle()
flappy.shape("flappyup.gif")
flappy.speed(1)
flappy.pu()
flappy.rt(90)

pipes = []

class Pipes(Turtle):
    
    def __init__(self, def_name = None):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        
        if def_name == None:
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
        self.defined_name = def_name
        
        self.giveshape()
        pipes.append(self)
        
    def giveshape(self):
        shapename = self.defined_name +".gif"
        s.register_shape(shapename)
        self.shape(shapename)

pipe15top = Pipes()
pipe20top = Pipes()
pipe30top = Pipes()
pipe40top = Pipes()
pipe45top = Pipes()

pipe15bottom = Pipes()
pipe20bottom = Pipes()
pipe30bottom = Pipes()
pipe40bottom = Pipes()
pipe45bottom = Pipes()

def Start():
    
    flappy.goto(-screen_width/2.6,0)
    
    pipe30top.goto(0,300)
    pipe30bottom.goto(0,-300)
    pipe20top.goto(400,370)
    pipe40bottom.goto(400,-250)
    pipe40top.goto(800,250)
    pipe20bottom.goto(800,-370)
    pipe15top.goto(1200,470)
    pipe45bottom.goto(1200,-150)
    pipe15bottom.goto(1650,-450)
    pipe45top.goto(1650,170)
    
    global t
    t = 0
    global u
    u = 10
    global f_alive
    f_alive = True

def Flap():
    global f_alive, falling, t, v, u
    if f_alive:
        falling = False
        t = 0
        u1 = 44.27188724235731
        flappy.shape("flappydown.gif")
        for i in range(2):
            v1 = u1 - 9.8*t
            flappy.bk(v1)
            t+=1
            s.update()
        t = 0
        u = 5 #10
        v = 0
        falling = True
        flappy.shape("flappyup.gif")

def Motion():
    global t, u, v
    
    t += 0.015
    v = u + 0.4# u + 10*t
    flappy.fd(v)
    u = v
    
    for pipe in pipes:
        pipe.setx(pipe.xcor()-9) #10
    
    s.update()
    

Start()

listen()
onkeypress(Flap, "f")


while True:

    while f_alive:
        
        Motion()

        if -630>pipe30top.xcor()>-870 and (flappy.ycor()<-70 or flappy.ycor()>69):
            f_alive = False
        
        if -630>pipe20top.xcor()>-870 and (flappy.ycor()<69 or flappy.ycor()>215):
            f_alive = False
        
        if -630>pipe40top.xcor()>-870 and (flappy.ycor()<-210 or flappy.ycor()>-65):
            f_alive = False
        
        if -630>pipe15top.xcor()>-870 and (flappy.ycor()<100 or flappy.ycor()>360):
            f_alive = False
            
        if -630>pipe45top.xcor()>-870 and (flappy.ycor()>-100 or flappy.ycor()<-350):
            f_alive = False
        
        if flappy.ycor()<-500 or flappy.ycor()>500:
            f_alive = False
    
        s.update()

    else:

        Start()
