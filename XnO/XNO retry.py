
from turtle import *
from random import *
from time import *
from os import *

chdir(getcwd())

s = Screen()
s.delay(0)
s.register_shape("X.gif")
s.register_shape("O.gif")

tno, turtles, playing = 0, [], True
boardspace = [[None,None,None],
              [None,None,None],
              [None,None,None]]
xnodict = {
    (-200.0, 200.0) : (0,0),
    (0.0, 200.0) : (0,1),
    (200.0, 200.0) : (0,2),
    (-200.0, 0.0) : (1,0),
    (0.0, 0.0) : (1,1),
    (200.0, 0.0) : (1,2),
    (-200.0, -200.0) : (2,0),
    (0.0, -200.0) : (2,1),
    (200.0, -200.0) : (2,2),
    }

t = Turtle()
t.speed(0)
t.pu()
t.ht()
for i in range(9): turtles.append(t.clone())
t.pensize(5)
t.pd()

def board():
    for k in range(2):
        if k == 1: t.rt(90)
        for i in range(2):
            t.pu()
            t.goto(-100 + 200*i,300) if k == 1 else t.goto(-300,-100 + 200*i)
            t.pd()
            t.fd(600)

def xno(x,y):
    global tno, boardspace, playing
    if playing:
        for i in range(3):
            for k in range(3):
                x1, x2, y1, y2 = (-300 + 200*k), (-300 + 200*(k+1)), (-300 + 200*i), (-300 + 200*(i+1))
                if (x1 < x < x2) and (y1 < y < y2):
                    pos = xnodict[((x1+x2) / 2, (y1+y2) / 2)]
                    if boardspace[pos[0]][pos[1]] == None:
                        boardspace[pos[0]][pos[1]], s = (True,turtles[tno].shape("X.gif")) if tno%2 == 0 else (False,turtles[tno].shape("O.gif"))
                        s = turtles[tno].goto(pos), turtles[tno].st()
                        tno += 1

board()
listen()
s.onscreenclick(xno)

while playing:
    for ch in True,False:
        cc = []
        for i in range(3): cc.append((i,i))
            
    s.update()
print("Finished")



