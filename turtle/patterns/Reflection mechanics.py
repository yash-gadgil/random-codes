

from turtle import *
import math


s = Screen()
s.delay(0)

'''
t = Turtle()
t.rt(30)
print(t.towards((4,3))) 
'''


class Ball(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.start = self.pos()

    def reflectx(self):
        self.end = self.pos()
        if self.start[0] == self.end[0] or self.start[1] == self.end[1]:
            angle = 180
            third = 0 ##
        else:
            third = (self.end[0],self.start[1])
            angle = (2*(180 - (self.towards(third) + (360 - self.heading()))))%360
        #print("start = {}\nend = {}\nthird = {}\nheading = {}".format(self.start,self.end,self.towards(third),self.heading())) ##
        self.rt(angle)
        self.start = self.end
        #print(angle) ##

    def reflecty(self):
        self.end = self.pos()
        if self.start[0] == self.end[0] or self.start[1] == self.end[1]:
            angle = 180
            third = 0 ##
        else:
            third = (self.end[1],self.start[0])
            angle = (2*(180 - (self.towards(third) + (360 - self.heading()))))%360
        #print("start = {}\nend = {}\nthird = {}\nheading = {}".format(self.start,self.end,self.towards(third),self.heading())) ##
        self.rt(angle)
        self.start = self.end
        #print(angle) ##


t = Ball()
t.speed(0)
t.goto(0,0) #(34,4) 45 #
t.rt(30) #37.5 #2 #36.84 #28.072 #38.5 #42 #21 # all for (0,0)
p = 0
ytop = 0

d = 0.1
while 1:
    if t.xcor() >= 150 or t.xcor() <= -150:
        t.reflectx()
        ytop = 0
    if (t.ycor() >= 150 or t.ycor() <= -150 ) and not ytop:
        t.reflecty()
        ytop = 1
    t.fd(1)
    t.rt(d) ## drift
    #d += 0.00001
         
# (0,0) 45 deg 0.1 drift 100x100
# (0,0) 30 deg 0.1 drift 100x100
# (0,0) 15 deg 0.1 drift 100x100
# (0,0) 42 deg 0.1 drift 100x100

'''
t = Turtle()
t.pu()
t.fd(100)
t.rt(90)
t.pd()
t.fd(100)
t.rt(90)
t.fd(200)



ball = Turtle()
#ball.shape("circle")
#ball.turtlesize(0.4)
#ball.pu()


ball.rt(30)

r = 0

while 1:

    if ball.xcor() >= 100:

        
            #t.goto(ball.pos())
            #t.rt(90)
            #t.fd(30)
        ball.rt((180 - ball.towards(0,0))*2)

        print("##")
        print(ball.towards(0,0))
        print((180 - ball.towards(0,0))*2)
        print("##")

    if ball.ycor() <= -100:

        if not r:
            t.goto(ball.pos())
            t.rt(90)
            t.fd(30)
            r = 1
            ball.rt((180 - ball.towards(0,0)))
        

    print(ball.pos())
    ball.fd(1)


ball.rt(30)

sp = (0,0)

t = 0
tt = 0


while 1:

    if ball.xcor() >= 100 and not t:
        angle = ball.towards(sp)
        print(angle)
        sp = ball.pos()
        ball.rt(120)
        t = 1

    if ball.ycor() <= -100:
        print(ball.towards(sp))
    
    ball.fd(1)


while 1:

    if ball.xcor() >= 100 and not t:
        angle = 360 - ball.heading()
        print(ball.heading())
        ball.rt(((90 - angle)*2)%360)
        print(((90 - angle)*2)%360)
        t = 1

    if ball.ycor() <= -100 and not tt:
        angle = 360 - ball.heading()
        print(ball.heading())
        ball.rt(((90 - angle)*2)%360)
        print(((90 - angle)*2)%360)
        tt = 1

    ball.fd(1)
'''
