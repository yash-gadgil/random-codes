
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

t = Turtle()
t.speed(0)
t.pensize(5)
t.ht()

tno = 0
turtles = []
boardspace = [None,None,None,None,None,None,None,None,None]
playing = True

playerX = True

if playerX:
    playerturn = True
else:
    playerturn = False

boardd = ""
recent = None

xnodict = {
    "(-200.0, -200.0)" : 0,
    "(0.0, -200.0)" : 1,
    "(200.0, -200.0)" : 2,
    "(-200.0, 0.0)" : 3,
    "(0.0, 0.0)" : 4,
    "(200.0, 0.0)" : 5,
    "(-200.0, 200.0)" : 6,
    "(0.0, 200.0)" : 7,
    "(200.0, 200.0)" : 8,
    
    "0" : (-200.0, -200.0),
    "1" : (0.0, -200.0),
    "2" : (200.0, -200.0),
    "3" : (-200.0, 0.0),
    "4" : (0.0, 0.0),
    "5" : (200.0, 0.0),
    "6" : (-200.0, 200.0),
    "7" : (0.0, 200.0),
    "8" : (200.0, 200.0)
    }

u = Turtle()
u.speed(0)
u.pu()
u.ht()

for i in range(9):
    turtles.append(u.clone())

def windef(a,b,c,boole):

    if (boardspace[a] != None) and (boardspace[b] != None) and (boardspace[c] != None):
        
        if (boardspace[a] == boole) and (boardspace[b] == boole) and (boardspace[c] == boole):

            return True
        
        else:

            return False
    
    else:

        return False

def comp():
    global tno, boardspace, playerturn, boardd

    moves = []
    boardd += str(recent)
    print(playing)

    if not playerturn and playing:

        for i in range(9):

            if str(i) not in boardd:

                moves.append(i)

        block = choice(moves)
        boardd += str(block)
            
        if tno%2 == 0:
                 
            turtles[tno].shape("X.gif")
            boardspace[block] = True
                
        else:
                
            turtles[tno].shape("O.gif")
            boardspace[block] = False

        turtles[tno].goto(xnodict[str(block)])
        turtles[tno].st()


        tno += 1
        playerturn = True

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

    global tno, boardspace, playerturn, recent

    if playing and playerturn:
        for i in range(3):
            
            for k in range(3):

                x1 = (-300 + 200*k)
                x2 = (-300 + 200*(k+1))

                y1 = (-300 + 200*i)
                y2 = (-300 + 200*(i+1))

                if (x1 < x < x2) and (y1 < y < y2):

                    pos = (x1+x2) / 2, (y1+y2) / 2
                    recent = xnodict[str(pos)]

                    if boardspace[recent] == None:

                        if tno%2 == 0:
                            boardspace[recent] = True
                            turtles[tno].shape("X.gif")
                        else:
                            boardspace[recent] = False
                            turtles[tno].shape("O.gif")

                        turtles[tno].goto(pos)
                        turtles[tno].st()

                        tno += 1
                        playerturn = False

def start():

    board()
    listen()
    s.onscreenclick(xno)

start()

while playing:

    if playerX:
        if tno%2 != 0:
            comp()
    else:
        if tno%2 == 0:
            comp()

    if windef(0,1,2,True) or windef(3,4,5,True) or windef(6,7,8,True) or windef(0,3,6,True) or windef(1,4,7,True) or windef(2,5,8,True) or windef(0,4,8,True) or windef(2,4,6,True):

        print("X wins!")
        playing = False

    elif windef(0,1,2,False) or windef(3,4,5,False) or windef(6,7,8,False) or windef(0,3,6,False) or windef(1,4,7,False) or windef(2,5,8,False) or windef(0,4,8,False) or windef(2,4,6,False):

        print("O wins!")
        playing = False

    elif tno >= 9:

        print("Tie!")
        playing = False

    s.update()
            
else:

    print("Finished")

