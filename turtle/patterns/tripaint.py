import turtle
import math

s=turtle.getscreen()
turtle.title("tri")
turtle.ht()
#s.bgcolor("black")
s.bgcolor("white")
s.delay(0)
#s.screensize(3000,5000)


t1 = turtle.Turtle()
t1.speed(0)
t1.pensize(3)
t1.fillcolor("#891300") #red

t2 = turtle.Turtle()
t2.speed(0)
t2.lt(120)
t2.pensize(3)
t2.fillcolor("#0D98BA") #green

t3 = turtle.Turtle()
t3.speed(0)
t3.rt(120)
t3.pensize(3)
t3.fillcolor("#00FFFF") #blue

t1.ht()
t2.ht()
t3.ht()

x = 5 #100
a = 60 #60

i = 0

while True:
    
    t1.begin_fill()
    t2.begin_fill()
    t3.begin_fill()
    
    t1.fd(x)
    t2.fd(x)
    t3.fd(x)

    t1.lt(a)
    t2.lt(a)
    t3.lt(a)

    t1.fd(x)
    t2.fd(x)
    t3.fd(x)

    t1.lt(a)
    t2.lt(a)
    t3.lt(a)

    t1.fd(2*x)
    t2.fd(2*x)
    t3.fd(2*x)

    t1.lt(2*a)
    t2.lt(2*a)
    t3.lt(2*a)

    t1.fd(2*x)
    t2.fd(2*x)
    t3.fd(2*x)

    t1.end_fill()
    t2.end_fill()
    t3.end_fill()

    t1.lt(a)
    t2.lt(a)
    t3.lt(a)

    t1.fd(x)
    t2.fd(x)
    t3.fd(x)
    
    a += 1 #0 #1
