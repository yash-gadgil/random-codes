

from turtle import *
from os import *

chdir(getcwd())

s = Screen()
s.delay(0)
title("Portal Test")
bgcolor("green")

s.register_shape("playerleft.gif")
s.register_shape("playerright.gif")
s.register_shape("portal1.gif")

world = []
portals = []
directions = {"W": (0,100),"A": (-100,0),"S": (0,-100),"D": (100,0)}
ticks = []
player_det = [1,1,0]


'''
class World():

    def __init__(self):
        self.world = []
        self.portals = []
'''      

class Player(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.shape("playerright.gif") if player_det[0] else self.shape("playerleft.gif")
        self.face = player_det[0] # 0 = Left | 1 = Right
        self.rb = player_det[1] # 0 = Red | 1 = Blue
        self.chosen = player_det[2] # 0 = Red | 1 = Blue
        listen()
        onkeypress(self.Up,'w')
        onkeypress(self.Left,'a')
        onkeypress(self.Down,'s')
        onkeypress(self.Right,'d')
        onkeypress(self.PW,'W')
        onkeypress(self.PA,'A')
        onkeypress(self.PS,'S')
        onkeypress(self.PD,'D')
        onkeypress(self.switch,'t')
        onkeypress(self.switch_chosen,'c')
        
    def Up(self):
        for i in world:
            i.sety(i.ycor()-25)

    def Down(self):
        for i in world:
            i.sety(i.ycor()+25)

    def Left(self):
        if self.face:
            self.shape("playerleft.gif")
            self.face = 0
        for i in world:
            i.setx(i.xcor()+25)

    def Right(self):
        if not self.face:
            self.shape("playerright.gif")
            self.face = 1
        for i in world:
            i.setx(i.xcor()-25)

    #portals.append(Portal(self.chosen if len(portals) == 2 else (0 if 0 not in [s.color for s in portals] else 1),"W"))
    #portals.append(Portal(0 if 0 not in [s.color for s in portals] else 1,"A"))
    #else:
    #portals.append(Portal(0 if 0 not in [s.color for s in portals] else 1,"A"))
    #len(portals) == 2:

    def PW(self):
        if len(portals) == 2 or self.chosen not in [ff.color for ff in portals]:
            for nu,o in enumerate(portals):
                if o.color == self.chosen:
                    o.ht()
                    del o,portals[nu]
            portals.append(Portal(self.chosen,"W"))
            self.ht()
            player_det = [self.face,self.rb,self.chosen]
            del player[0], self    ######## specific list player
            player.append(Player()) ######## specific list player
        #self.shape("playerright.gif") if self.face else self.shape("playerleft.gif")

    def PA(self):
        if len(portals) == 2 or self.chosen not in [ff.color for ff in portals]: 
            for nu,o in enumerate(portals):
                if o.color == self.chosen:
                    o.ht()
                    del o,portals[nu]
            portals.append(Portal(self.chosen,"A"))
            self.ht()
            player_det = [self.face,self.rb,self.chosen]
            del player[0], self
            player.append(Player())
            player[0].shape("playerleft.gif")
            player[0].face = 0
            
        #self.shape("playerleft.gif") #self.shape("playerright.gif") if self.face else 

    def PS(self):
        if len(portals) == 2 or self.chosen not in [ff.color for ff in portals]:
            for nu,o in enumerate(portals):
                if o.color == self.chosen:
                    o.ht()
                    del o,portals[nu]
            portals.append(Portal(self.chosen,"S"))
            self.ht()
            player_det = [self.face,self.rb,self.chosen]
            del player[0], self
            player.append(Player())
        #self.shape("playerright.gif") if self.face else self.shape("playerleft.gif")

    def PD(self):
        if len(portals) == 2 or self.chosen not in [ff.color for ff in portals]:
            for nu,o in enumerate(portals):
                if o.color == self.chosen:
                    o.ht()
                    del o,portals[nu]
            portals.append(Portal(self.chosen,"D"))
            self.ht()
            player_det = [self.face,self.rb,self.chosen]
            del player[0], self
            player.append(Player())
            player[0].shape("playerright.gif")
            player[0].face = 1
        #self.shape("playerright.gif") #if self.face else self.shape("playerleft.gif")

    def switch(self):
        self.rb = not self.rb

    def switch_chosen(self):
        self.chosen = not self.chosen

    
        
class Portal(Turtle):

    def __init__(self,color,di):
        Turtle.__init__(self)
        self.speed(0)
        self.shape("portal1.gif")
        world.append(self)
        #portals.append(self)
        self.color = color # 0 = Red | 1 = Blue
        self.di = di # W = up | A = left | S = down | D = right
        self.pu()
        self.goto(directions[di])
        ticks.append(self.teleport_cond)
        
    def teleport(self):
        if self.color != player[0].rb: # for specific player in list player
            return
        for k in portals:
            if not self.color == k.color:
                xk, yk, xs, ys = k.xcor(), k.ycor(), self.xcor(), self.ycor()
                for l in world:
                    l.setx(l.xcor() - xk + xs) # l.setx(l.xcor() - k.xcor() + self.xcor())
                    l.sety(l.ycor() - yk + ys) # l.sety(l.ycor() - k.ycor() + self.ycor())
             

    def teleport_cond(self):
        if -50 < self.xcor() < 50 and -50 < self.ycor() < 50:
            self.teleport()
                    
        
player = [Player()]

while 1:

    #print(player)

    #for portal in portals:

        #if -50<portal.xcor()<50 and -50<portal.ycor()<50:
            #portal.teleport()

    for tick in ticks:
        tick()

    s.update()
