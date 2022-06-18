
from turtle import *
from os import *

chdir(getcwd())

s = Screen()
s.delay(0)
for i in "X.gif","O.gif": s.register_shape(i)

t = Turtle()
t.speed(0)
t.pensize(5)
t.ht()

tno, turtles, boardspace, playing = 0, [], [None,None,None,None,None,None,None,None,None], True
xnodict = {
    "(-200.0, -200.0)" : 0,
    "(0.0, -200.0)" : 1,
    "(200.0, -200.0)" : 2,
    "(-200.0, 0.0)" : 3,
    "(0.0, 0.0)" : 4,
    "(200.0, 0.0)" : 5,
    "(-200.0, 200.0)" : 6,
    "(0.0, 200.0)" : 7,
    "(200.0, 200.0)" : 8
    }

u = Turtle()
u.speed(0)
u.pu()
u.ht()
for i in range(9): turtles.append(u.clone())

def windef(a,b,c,boole): return (True if (boardspace[a] == boole) and (boardspace[b] == boole) and (boardspace[c] == boole) else False) if (boardspace[a] != None) and (boardspace[b] != None) and (boardspace[c] != None) else False 
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
                    pos = ((x1+x2) / 2, (y1+y2) / 2)
                    occ = str(pos)
                    if boardspace[xnodict[occ]] == None:
                        boardspace[xnodict[occ]], s = (True,turtles[tno].shape("X.gif")) if tno%2 == 0 else (False,turtles[tno].shape("O.gif"))
                        s = turtles[tno].goto(pos), turtles[tno].st()
                        tno += 1
board()
listen()
s.onscreenclick(xno)
while playing:
    if windef(0,1,2,True) or windef(3,4,5,True) or windef(6,7,8,True) or windef(0,3,6,True) or windef(1,4,7,True) or windef(2,5,8,True) or windef(0,4,8,True) or windef(2,4,6,True): playing, ses = False, print("X wins!")
    elif windef(0,1,2,False) or windef(3,4,5,False) or windef(6,7,8,False) or windef(0,3,6,False) or windef(1,4,7,False) or windef(2,5,8,False) or windef(0,4,8,False) or windef(2,4,6,False): playing, ses = False, print("O wins!")
    elif tno == 9: playing, ses = False, print("Tie!")
    s.update()  
print("Finished")
