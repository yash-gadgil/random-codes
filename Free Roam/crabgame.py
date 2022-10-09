
from turtle import *
from os import *
import tkinter

info = tkinter.Tk()
screen_width = info.winfo_screenwidth()
screen_height = info.winfo_screenheight()
info.destroy()

files_path = getcwd()
chdir(files_path)

s = Screen()
s.delay(0)
title("Crab Game")
bgcolor("#0FFFFF")

height, width = 900, 1500

setup(width = width, height = height)

s.register_shape("playerright.gif")
s.register_shape("playerleft.gif")
s.register_shape("chasercrab.gif")

t = Turtle()
t.shape("playerright.gif")
t.speed(0)
t.pu()

c = Turtle()
c.shape("chasercrab.gif")
c.speed(1)
c.pu()
c.goto(100,100)

scale = 50
alive = True

def PlayerRight():
    t.shape("playerright.gif")
    if t.xcor() < (width/2):
        t.setx(t.xcor() + scale)

def PlayerLeft():
    t.shape("playerleft.gif")
    if t.xcor() > (-width/2):
        t.setx(t.xcor() - scale)

def PlayerUp():
    if t.ycor() < (height/2):
        t.sety(t.ycor() + scale)

def PlayerDown():
    if t.ycor() > (-height/2):
        t.sety(t.ycor() - scale)

listen()
onkeypress(PlayerUp,"w")
onkeypress(PlayerDown,"s")
onkeypress(PlayerRight,"d")
onkeypress(PlayerLeft,"a")

while 1:
    
    while alive:

        c.setheading(c.towards(t.pos()))
        c.fd(0.21) #0.13
        alive = not 0 < c.distance(t) < 7
        s.update()
    
    alive = True
    c.goto(100,100)
    t.goto(0,0)           
