import turtle
import math

s=turtle.getscreen()
turtle.title("Triangle Maker")
turtle.ht()
s.bgcolor("red")

#t = turtle.Turtle()
#t.speed(0)
#t.penup()

t = turtle.Turtle()
t.speed(0)
#t.pensize(2)
t.penup()

#t.goto(-200,-200)
t.goto(-600,-400)
t.pendown()

phi = ( 1 + math.sqrt(5) ) / 2
phi0 = phi - 1

x = 900

t.lt(90)
t.ht()
#t.begin_fill()
for i in range(16):
    t.begin_fill()
    t.circle(-x/phi**i,90)
    t.end_fill()
#t.end_fill()


'''
t.pendown()
t.fd(x)
t.lt(90)
t.fd(x)
t.lt(90)
t.fd(x)
t.lt(90)
t.fd(x)
t.lt(90)
t.fd(x*phi)
t.lt(90)
t.fd(x)
t.lt(90)
t.fd(x*phi0)
t.lt(90)
t.fd(x/phi)
t.lt(90)
t.fd(x*phi0)
t.rt(90)
t.fd(x*phi0**2)
t.rt(90)
t.fd(x*phi0/phi)
t.rt(90)
t.fd(x*phi0**2)
t.bk(x*phi0**2)
t.fd(x*phi0**3)
t.lt(90)
t.fd(x*phi0**3)
t.rt(90)
t.fd(x*phi0**4)
t.rt(90)
t.fd(x*phi0**4)
t.rt(90)
t.fd(x*phi0**4)
t.bk(x*phi0**4)
t.fd(x*phi0**4/phi)
t.lt(90)
t.fd(x*phi0**4/phi)
'''