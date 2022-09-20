
from turtle import *
from os import *
from time import *

chdir(getcwd())

s = Screen()
s.delay(0)
title("Animation Test")
bgcolor("green")

for k in range(1,3):
    for i in range(8):
        s.register_shape("frame_" + str(i) + "_delay-0." + str(k) + "s.gif")

world = []
#t = 0

class Player(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.shape("frame_0_delay-0.1s.gif") #if player_det[0] else self.shape("playerleft.gif")
        self.face = 1 # 0 = Left | 1 = Right
        self.walk = 0
        listen()
        onkeypress(self.Up,'w')
        onkeypress(self.Left,'a')
        onkeypress(self.Down,'s')
        onkeypress(self.Right,'d')

    def Up(self):
        for i in world:
            i.sety(i.ycor()-25)

    def Down(self):
        for i in world:
            i.sety(i.ycor()+25)

    def Left(self):
        self.walk = (self.walk + 1) % 8 if not self.face else 0
        self.shape("frame_" + str(self.walk) + "_delay-0.2s.gif")
        self.face = 0
        #t = 0
        for i in world:
            i.setx(i.xcor()+25)

    def Right(self):
        self.walk = (self.walk + 1) % 8 if self.face else 0
        self.shape("frame_" + str(self.walk) + "_delay-0.1s.gif")
        self.face = 1
        #t = 0
        for i in world:
            i.setx(i.xcor()-25)

p = Player()

'''
while 1:
    #sleep(1)
    t += 1
    if t > 10:
        p.shape("frame_0_delay-0.1s.gif" if p.face else "frame_0_delay-0.2s.gif")
    #s.update()
'''
