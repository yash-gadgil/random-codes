
from turtle import *
from os import *
from random import *

chdir(getcwd())

s = Screen()
s.delay(0)
title("World Generator")
bgcolor("green")

s.register_shape("playerleft.gif")
s.register_shape("playerright.gif")
s.register_shape("tree1.gif")
s.register_shape("rock1.gif")

#x_ax, y_ax = randrange(100,200,25),randrange(100,200,25)
#x_ax, y_ax = randrange(4,8),randrange(2,4)
#print(x_ax,y_ax)

#world = [["t" if randrange(1,100) <= 5 else ""  for k in range(2*x_ax//25)] for i in range(2*y_ax//25)]
#generator = [["t" if randrange(1,100) <= 5 else ""  for k in list(range(-x_ax,0,-1)) + list(range(x_ax))] for i in list(range(-y_ax,0,-1)) + list(range(y_ax))]
#print(range(-y_ax,y_ax + 1))

gap = 125
chance = 10

#generator = [(k * gap,i * gap) for k in range(-x_ax,x_ax + 1) for i in range(-y_ax,y_ax + 1) ]
#print(generator)
world = []

#for k in generator:
    #print(k)

#print(list(range(0,2*x_ax,25)))

class World():
    

    def __init__(self):
        self.x_ax, self.y_ax = randrange(4,8),randrange(2,4)
        self.minimap = [(k * gap,i * gap) for k in range(-self.x_ax, self.x_ax + 1) for i in range(-self.y_ax, self.y_ax + 1) ]
        self.trees = []
        self.rocks = []
        self.centre = [Turtle()]
        self.centre[0].ht()
        self.centre[0].speed(0)
        self.centre[0].pu()
        world.append(self.centre[0])

        #generator = [(k * gap,i * gap) for k in range(-x_ax,x_ax + 1) for i in range(-y_ax,y_ax + 1) ]

        #p = Player()

        for i in self.minimap[::-1]:

            if randrange(1,100) <= chance:
                self.trees.append(Tree())
                world.append(self.trees[-1])
                self.trees[-1].goto(i[0],i[1])
                continue
            if randrange(1,100) <= 10:
                self.rocks.append(Rock())
                world.append(self.rocks[-1])
                self.rocks[-1].goto(i[0],i[1])
                continue
        

    #@classmethod
    def edge(self,wall):
        if wall in "a":
            return self.centre[0].xcor() == self.x_ax * gap #centre[0].xcor()
        elif wall in "s":
            return self.centre[0].ycor() == self.y_ax * gap #centre[0].ycor()
        elif wall in "w":
            return -self.centre[0].ycor() == self.y_ax * gap
        elif wall in "d":
            return -self.centre[0].xcor() == self.x_ax * gap
        #print(world)
        
        
        '''
        for y,i in enumerate(self.minimap):
            print(y,i)
            
            if y <= y_ax:
                ycord = (y - y_ax//25) #* 5 #* 25
            else:
                ycord = (y_ax//25 - y) #* 5
            
            ycord = i * 25
            for x,k in enumerate(i):
                
                if x <= x_ax:
                    xcord = (x - x_ax//25) #* 5 #* 25
                else:
                    xcord = (x_ax//25 - x) #* 5
                
                xcord = k * 25
                if k == 't':
                    print(xcord,ycord)
                    self.trees.append(Tree())
                    world.append(self.trees[-1])
                    self.trees[-1].goto(xcord,ycord) #*25
        '''
        

class Player(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.shape("playerright.gif") #if player_det[0] else self.shape("playerleft.gif")
        self.face = 1 # 0 = Left | 1 = Right
        listen()
        onkeypress(self.Up,'w')
        onkeypress(self.Left,'a')
        onkeypress(self.Down,'s')
        onkeypress(self.Right,'d')

    def Up(self):
        if not w.edge("w"): ##
            for i in world:
                i.sety(i.ycor()-25)

    def Down(self):
        if not w.edge("s"): ##
            for i in world:
                i.sety(i.ycor()+25)

    def Left(self):
        if self.face:
            self.shape("playerleft.gif")
            self.face = 0
        if not w.edge("a"): ##
            for i in world:
                i.setx(i.xcor()+25)

    def Right(self):
        if not self.face:
            self.shape("playerright.gif")
            self.face = 1
        if not w.edge("d"): ##
            for i in world:
                i.setx(i.xcor()-25)

        
            
class Tree(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.shape("tree1.gif")
        self.pu()
        #print(self.turtlesize())

class Rock(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.shape("rock1.gif")
        self.pu()
    
p = Player()
w = World()

while 1:
    s.update()
#t = Tree()
