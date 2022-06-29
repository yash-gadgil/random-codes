
from turtle import *
from random import *
from time import *
from os import *

files_path = getcwd()
chdir(files_path)

s = Screen()
s.delay(0)
s.register_shape("X.gif")
s.register_shape("O.gif")

tno, turtles, playing, xnodict = 0, [], True, {}
boardspace = [[None,None,None],
              [None,None,None],
              [None,None,None]]
for i in [-200.,0.,200.]:
    for k in [-200.,0.,200.]:
        xnodict[(k, i)] = tno
        tno += 1
t = Turtle()
t.speed(0)
t.pensize(5)
t.ht()
t.pu()
for i in range(9):
    turtles.append(t.clone())
t.pd()

def outcome():
    for i in boardspace:
        temp = i[0]
        for k in range(1,3):
            if i[k] != None:
                if temp == k:
                    continue
                else:
                    break
            else:
                break
        else:
            return k
    

def board():
    for k in range(2):
        if k == 1:
            t.rt(90)
        for i in range(2):
            t.pu()
            if k == 1:
                t.goto(-100 + 200*i,300)
            else:
                t.goto(-300,-100 + 200*i)
            t.pd()
            t.fd(600)

def xno(x,y):
    global tno, boardspace, playing
    if playing:
        for i in range(3):
            for k in range(3):
                x1, x2, y1, y2 = (-300 + 200*k), (-300 + 200*(k+1)), (-300 + 200*i), (-300 + 200*(i+1))
                if (x1 < x < x2) and (y1 < y < y2):
                    pos = (x1+x2) / 2, (y1+y2) / 2
                    if boardspace[xnodict[pos]] == None:
                        if tno%2 == 0:
                            boardspace[xnodict[pos]] = True
                            turtles[tno].shape("X.gif")
                        else:
                            boardspace[xnodict[pos]] = False
                            turtles[tno].shape("O.gif")
                        turtles[tno].goto(pos)
                        turtles[tno].st()
                        tno += 1
