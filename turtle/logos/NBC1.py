
from turtle import *

s = Screen()
title("NBC Logo")

t = Turtle()
t.speed(0)
t.pensize(2)
t.pencolor("#0DB14B")

f = 18.75

def going(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

def pfeather(color):
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)
    t.fd(173.9)
    t.circle(50,211.5)
    t.fd(173.9)
    t.end_fill()

def nfeather(color):
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)
    t.fd(173.9)
    t.circle(-50,211.5)
    t.fd(173.9)
    t.end_fill()

for i in (1,"#0DB14B","#0089D0","#6460AA"),(-1,"#FCB711","#F37021","#CC004C"):
    going(f*i[0],0)
    pfeather(i[1])

    t.pu()
    t.home()
    t.fd(f*i[0])
    t.fd(10.5)
    t.rt(90)
    t.fd(21.3)
    t.lt(57.9)
    t.pd()
    


