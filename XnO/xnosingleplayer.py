
from random import *
from turtle import *
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
playerturn = True

#(boardspace[0] and boardspace[1] and boardspace[2]) or (boardspace[3] and boardspace[4] and boardspace[5]) or (boardspace[6] and boardspace[7] and boardspace[8]) or (boardspace[0] and boardspace[3] and boardspace[6]) or\
#(boardspace[1] and boardspace[4] and boardspace[7]) or (boardspace[2] and boardspace[5] and boardspace[8]) or (boardspace[0] and boardspace[4] and boardspace[8]) or (boardspace[2] and boardspace[4] and boardspace[6])

#windef(0,1,2,False) (boardspace[0] == False and boardspace[1] == False and boardspace[2] == False)

'''
adjm = {
    "1" : [2,5,4,3,0],
    "3" : [0,1,4,7,6],
    "7" : [6,3,4,5,8],
    "5" : [8,7,4,1,2],
    }
'''

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

def determiner(a,b,c,boole):
    global tno, boardspace, playerturn

    empty = 0
    line = [a,b,c]
    emptyblock = []

    if boole:
        turtles[tno].shape("O.gif")
    else:
        turtles[tno].shape("X.gif")

    for i in line:

        if boardspace[i] == None:

            emptyblock.append(i)

            empty += 1
            #print("empty =",empty)

    if empty == 1:
        
        line.remove(emptyblock[0])
        occc = 0

        for k in line:

            if boardspace[k] == boole:
                occc += 1

        if occc == 2:

            turtles[tno].goto(xnodict[str(emptyblock[0])])
            turtles[tno].st()

            boardspace[emptyblock[0]] = not boole

            tno += 1
            playerturn = True

    elif empty == 2:
        

        line.remove(emptyblock[0])
        line.remove(emptyblock[1])

        #print(line)

        if boardspace[line[0]] == boole:
            #print("here")

            chosen = choice(emptyblock)

            turtles[tno].goto(xnodict[str(chosen)])
            turtles[tno].st()

            boardspace[chosen] = not boole

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

def comp():
    global playerturn, tno, boardspace

    if not playerturn:

        pass
        

def xno(x,y):

    global tno, boardspace, playing, playerturn

    if playing and playerturn:
        for i in range(3):
            
            for k in range(3):

                x1 = (-300 + 200*k)
                x2 = (-300 + 200*(k+1))

                y1 = (-300 + 200*i)
                y2 = (-300 + 200*(i+1))

                if (x1 < x < x2) and (y1 < y < y2):

                    pos = (x1+x2) / 2, (y1+y2) / 2
                    occ = str(pos)

                    if tno%2 == 0:
                        boardspace[xnodict[occ]] = True
                        turtles[tno].shape("X.gif")
                    else:
                        boardspace[xnodict[occ]] = False
                        turtles[tno].shape("O.gif")

                    turtles[tno].goto(pos)
                    turtles[tno].st()

                    tno += 1
                    playerturn = False

        if windef(0,1,2,True) or windef(3,4,5,True) or windef(6,7,8,True) or windef(0,3,6,True) or windef(1,4,7,True) or windef(2,5,8,True) or windef(0,4,8,True) or windef(2,4,6,True):

            print("X wins!")
            playing = False

        elif windef(0,1,2,False) or windef(3,4,5,False) or windef(6,7,8,False) or windef(0,3,6,False) or windef(1,4,7,False) or windef(2,5,8,False) or windef(0,4,8,False) or windef(2,4,6,False):

            print("O wins!")
            playing = False

        elif tno == 9:

            print("Tie!")
            playing = False

        


board()
listen()
s.onscreenclick(xno)

while playing:

    comp()

    s.update()
            
else:

    print("Finished")


