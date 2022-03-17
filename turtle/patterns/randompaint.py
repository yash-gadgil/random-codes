import turtle
from random import *

s=turtle.getscreen()
turtle.title("Shuriken")
turtle.ht()
#s.bgcolor("black")
s.bgcolor("white")

t1 = turtle.Turtle()
t1.speed(0)
t1.pensize(3)
t1.fillcolor("#891300") #red

t2 = turtle.Turtle()
t2.speed(0)
t2.lt(90)
t2.pensize(3)
t2.fillcolor("#0D98BA") #green

t3 = turtle.Turtle()
t3.speed(0)
t3.lt(180)
t3.pensize(3)
t3.fillcolor("#00FFFF") #blue

t4 = turtle.Turtle()
t4.speed(0)
t4.rt(90)
t4.pensize(3)
t4.fillcolor("#FDDA0D") #yellow

t1.ht()
t2.ht()
t3.ht()
t4.ht()

x = 25
a = 90
t = 0

'''
def look():
    t1.setheading(t1.towards(t2.pos()))
    t2.setheading(t2.towards(t3.pos()))
    t3.setheading(t4.towards(t4.pos()))
    t4.setheading(t4.towards(t1.pos()))

turtle.listen()
turtle.onkeypress(look,"w")
'''

while True:
    t1.begin_fill()
    t2.begin_fill()
    t3.begin_fill()
    t4.begin_fill()

    t1.fd(x)
    t2.fd(x)
    t3.fd(x)
    t4.fd(x)

    t1.lt(a)
    t2.rt(a)
    t3.lt(a)
    t4.rt(a)

    t1.bk(x)
    t2.bk(x)
    t3.bk(x)
    t4.bk(x)

    t1.rt(a/2)
    t2.lt(a/2)
    t3.rt(a/2)
    t4.lt(a/2)

    t1.circle(x,a)
    t2.circle(x,a)
    t3.circle(x,a)
    t4.circle(x,a)

    t1.bk(x)
    t2.bk(x)
    t3.bk(x)
    t4.bk(x)

    t1.end_fill()
    t2.end_fill()
    t3.end_fill()
    t4.end_fill()

    t1.lt(a*2)
    t2.rt(a)
    t3.lt(a*2)
    t4.rt(a)

    t1.fd(x)
    t2.fd(x)
    t3.fd(x)
    t4.fd(x)
    
    a -= 345

    t1.begin_fill()
    t2.begin_fill()
    t3.begin_fill()
    t4.begin_fill()

    t1.rt(a*2)
    t2.lt(a)
    t3.rt(a*2)
    t4.lt(a)
    
    
    if a%10 != 0:
        t1.circle(x,a/2)
        t2.circle(x,a/2)
        t3.circle(x,a/2)
        t4.circle(x,a/2)
    else:
        t1.circle(x,a)
        t2.circle(x,a)
        t3.circle(x,a)
        t4.circle(x,a)

    t1.end_fill()
    t2.end_fill()
    t3.end_fill()
    t4.end_fill()
    
    if a!=0 and a%10 == 0 :
        t1.fd(x/a)
        t2.fd(x/a)
        t3.fd(x/a)
        t4.fd(x/a)
    else:
        t1.fd(a)
        t2.fd(a)
        t3.fd(a)
        t4.fd(a)
    
    a += 360 + randint(0,1)*15
    t += 1

    if t == 10:
        a = a%360
        t = 0
