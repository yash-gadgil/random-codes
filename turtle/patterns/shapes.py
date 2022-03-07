

from turtle import *


s = Screen()
s.delay(0)


t = Turtle()
t.speed(0)
t.ht()

t.pu()
t.goto(0,0) #(0,-725)
t.pd()


#color = 900000
'''
x = 1  #1  #1  #1  #1  #1  #1  #1
a = 15 #15 #15 #15 #15 #15 #15 #15

while 1:
    t.fd(x)
    t.rt(a)
    #t.color("#{}".format(color))
    t.begin_fill()
    t.fd(3*x)
    t.rt(a*2)
    t.fd(x)
    t.rt(a*1.5)
    t.circle(x*4,120)
    t.rt(90)
    t.fd(10*x)
    t.end_fill()
    t.lt(a+30)
    a += 181 #1 #16 #22 #81 #4 #144 #169
    a %= 360
    #color += a
'''
'''
x = 1 
a = 15

while 1:
    t.fd(x)
    t.rt(a)
    t.begin_fill()
    t.fd(a*x/50)
    t.rt(a*2)
    t.fd(a/50)
    t.rt(a*1.5)
    t.circle(x*4,81)
    t.end_fill()
    t.rt(a)
    t.fd(10*x)
    t.lt(a+30)
    a += 180
    a %= 360
'''
'''
x = 5
a = 30
i = 1
b = 1

while 1:
    t.fd(x)
    t.rt(a)
    t.fd(x * i)
    t.lt(b * i)

    a += a/2 + 15 * (not i)
    a %= 360
    i = not i
    b += 1
    b %= 360
'''
'''
x = 1
a = 30
i = 1
b = 6
c = 1

while 1:
    t.fd(x)
    t.rt(a)
    t.fd(x * i)
    t.rt(b * i)
    t.circle(x,(a+b)%360)

    a += b/c + 30 * (not i)
    a %= 360
    b += a * i
    b %= 360
    c = c%60 + 1
    i = not i
'''
'''
x = 20
a = 30

def sharingan(x,a):
    t.rt(90 + a)
    t.begin_fill()
    t.circle(-x,270) #x 20
    t.lt(7.5) #rt
    t.circle(-x*3,60) #x*3 60
    t.lt(210) #rt
    t.circle(x*3,35.5) #-x*3 -60
    t.end_fill()

def sharingan1(x,a):
    t.rt(90 + a)
    t.begin_fill()
    t.circle(-x,285) #x 20
    t.lt(7.5) #rt
    t.circle(-x*2,60) #x*3 60
    t.lt(210) #rt
    t.circle(x*2,35.5) #-x*3 -60
    t.end_fill()

t.circle(100,60)
p = t.pos()
sharingan1(15,120)
t.pu()
t.home()
t.pd()
t.circle(100,175)
sharingan1(15,120)
t.pu()
t.home()
t.pd()
t.circle(100,300)
sharingan1(15,120)
t.pu()
t.home()
t.pd()
t.circle(100)
'''
'''
sharingan(10,60)
t.pu()
t.home()
t.goto(-200,0)
t.pd()
sharingan(10,120)
t.pu()
t.home()
t.goto(-100,150)
t.pd()
sharingan(10,-90)
'''
'''
t.st()
t.shape("circle")
t.shapesize(0.1, 0.1)
x,y = -0.7, -0.6

while 1:
    xcor = x**2 - y**2 + 0.9*x - 0.6*y
    ycor = 2*x*y + 2*x + 0.5*y

    x,y = xcor,ycor

    t.pu()
    t.goto(x,y)
    t.pd()
    t.stamp()
'''
'''
x = 1
a = 13
i = 0

while 1:
    t.circle(-x,a * 9)
    t.lt(7.5) 
    t.circle(-x*3,a * 2)
    t.lt(210)
    t.circle(x*3,a * 1.1834)
    t.rt(a * 3)
    t.fd(x*3)
    t.rt(a * i)
    
    a += 16.7
    a %= 360
    i = not i
'''
'''
x = 2
a = 90
y = 15

while 1:
    t.fd(x)
    t.rt(a)
    #t.begin_fill()
    t.circle(x*2,a*2)
    #t.end_fill()
    t.rt(a)
    t.fd(x)
    t.lt(a)

    a += y
    a %= 360
    y += 2
    y %= 90
'''

radians()
from math import *
t.goto(-10,15) #(12,13)

x = 14
i = 0

while 1:
    p = t.pos()
    p1 = (p[0]/sqrt(p[0]**2 + p[1]**2),p[1]/sqrt(p[0]**2 + p[1]**2))
    t.rt(p[0]*i + p[1]*(not i))
    t.fd(x)
    i = not i
