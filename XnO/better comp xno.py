
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

board = ""
recent = None
corners = [0,2,6,8]
mids = [1,3,5,7]

win2 = {
    "01" : 2,
    "10" : 2,
    "02" : 1,
    "20" : 1,
    "21" : 0,
    "12" : 0,
    
    "45" : 3,
    "54" : 3,
    "35" : 4,
    "53" : 4,
    "34" : 5,
    "43" : 5,

    "87" : 6,
    "78" : 6,
    "68" : 7,
    "86" : 7,
    "67" : 8,
    "76" : 8,

    "85" : 2,
    "58" : 2,
    "47" : 1,
    "74" : 1,
    "36" : 0,
    "63" : 0,
    
    "06" : 3,
    "60" : 3,
    "17" : 4,
    "71" : 4,
    "28" : 5,
    "82" : 5,

    "03" : 6,
    "30" : 6,
    "14" : 7,
    "41" : 7,
    "25" : 8,
    "52" : 8,

    "26" : 4,
    "62" : 4,
    "80" : 4,
    "08" : 4,
    "42" : 6,
    "24" : 6,
    "64" : 2,
    "46" : 2,
    "04" : 8,
    "40" : 8,
    "48" : 0,
    "84" : 0,
    }

opposite = {
    "0" : 8,
    "1" : 7,
    "2" : 6,
    "3" : 5,
    "5" : 3,
    "6" : 2,
    "7" : 1,
    "8" : 0
    }

adjc = {
    "0" : [1,4,3],
    "2" : [5,4,1],
    "6" : [3,4,7],
    "8" : [7,4,5],
    }

adjm = {
    "1" : [2,4,0],
    "3" : [0,4,6],
    "7" : [6,4,8],
    "5" : [8,4,2],
    }

mid = {
    "08" : 4,
    "80" : 4,
    "62" : 4,
    "26" : 4,
    "17" : 4,
    "71" : 4,
    "35" : 4,
    "53" : 4,
    "06" : 3,
    "60" : 3,
    "28" : 5,
    "82" : 5,
    "68" : 7,
    "86" : 7,
    "02" : 1,
    "20" : 1,
    }

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
    global tno, boardspace, playerturn, corners, recent, board

    if not playerturn and playing:

        if tno == 0:

            block = choice([0,2,4,6,8])
            board = str(block)

        elif tno == 1: 

            if recent == 4:

                block = choice(corners)
                board = "4" + str(block)

            else:

                block = 4
                board = str(recent) + "4"

        elif tno == 2:
            
            board += str(recent)

            if int(board[0]) in corners:

                if board[1] == "4":

                    corners.remove(int(board[0]))
                    cornersleft = corners.copy()
                    corners.append(int(board[0]))
                    
                    block = choice(cornersleft)
                    board += str(block)

                else:

                    block = 4
                    board += "4"

            elif board[0] == "4":

                if recent in corners:

                    corners.remove(recent)
                    cornersleft = corners.copy()
                    corners.append(recent)

                    block = choice(cornersleft)
                    board += str(block)

                else:

                    block = choice(corners)
                    board += str(block)

        elif tno == 3:

            board += str(recent)

            if board[1] == "4":

                if int(board[0]) in corners:

                    if recent == opposite[board[0]]:

                        block = choice(mids)
                        board += str(block)

                    elif recent in corners:

                        block = mid[board[0] + board[2]]
                        board += str(block)

                    elif recent in adjc[board[0]]:

                        block = win2[board[2] + board[0]]
                        board += str(block)

                    else:
                        
                        rl = list(xnodict[board[2]])
                        ol = list(xnodict[board[0]])

                        for i in range(2):

                            if rl[i] != 0:

                                if rl[i] > ol[i]:

                                    ol[i] = ol[i] + 200
                                    ol = tuple(ol)

                                    block = xnodict[str(ol)]
                                    board += str(block)

                                elif rl[i] < ol[i]:

                                    ol[i] = ol[i] - 200
                                    ol = tuple(ol)

                                    block = xnodict[str(ol)]
                                    board += str(block)

                else:

                    if recent == opposite[board[0]]:

                        block = choice(corners)
                        board += str(block)

                    elif recent in corners:

                        if recent in adjm[board[0]]:

                            block = win2[board[2] + board[0]]
                            board += str(block)

                        else:

                            rl = list(xnodict[board[0]])
                            ol = list(xnodict[board[2]])

                            for i in range(2):

                                if rl[i] != 0:

                                    if rl[i] > ol[i]:

                                        ol[i] = ol[i] + 200
                                        ol = tuple(ol)

                                        block = xnodict[str(ol)]
                                        board += str(block)

                                    elif rl[i] < ol[i]:

                                        ol[i] = ol[i] - 200
                                        ol = tuple(ol)

                                        block = xnodict[str(ol)]
                                        board += str(block)

                    else:

                        moves = adjm[board[2]] + adjm[board[0]]
                        mm = ""

                        for i in range(2):
                            moves.remove(4)

                        for i in moves:

                            if str(i) in mm:

                                mm = i
                                break

                            mm += str(i)

                        moves.remove(i)
                        moves.remove(i)

                        block = choice(moves)
                        board += str(block)
            else:

                if recent == opposite[board[1]]:

                    corners.remove(recent)
                    corners.remove(int(board[1]))
                    cornersleft = corners.copy()
                    corners.append(recent)
                    corners.append(int(board[1]))

                    block = choice(cornersleft)
                    board += str(block)

                else:

                    block = win2[board[2] + board[0]]
                    board += str(block)

        elif tno == 4:

            board += str(recent)

            if (board[0] == "4") or (board[2] == "4"):

                if str(win2[board[0] + board[2]]) not in board:

                    block = win2[board[0] + board[2]]
                    board += str(block)

                else:

                    try:

                        block = win2[board[1] + board[3]]
                        board += str(block)

                    except:

                        for k in [1,3]:

                            if int(board[k]) not in corners:

                                for i in adjm[board[k]]:

                                    if str(i) not in board:

                                        block = opposite[str(i)]
                                        board += str(block)

            else:

                if int(board[0]) == opposite[board[3]]:

                    block = win2[board[1] + board[3]]
                    board += str(block)

                else:

                    if str(win2[board[0] + board[2]]) not in board:

                        block = win2[board[0] + board[2]]
                        board += str(block)

                    else:

                        block = win2[board[1] + board[3]]
                        board += str(block)

        elif tno == 5:

            board += str(recent)

            tt = 0

            try:

                if str(win2[board[1] + board[3]]) not in board:

                    block = win2[board[1] + board[3]]
                    board += str(block)

                    tt += 1
                    
            except:

                pass

            if tt != 1:

                tt = 0

                for i in [0,2,4]:

                    try:

                        if i == 4:

                            k = 0

                        else:

                            k = i + 2

                        if str(win2[board[i] + board[k]]) not in board:

                            block = win2[board[i] + board[k]]
                            board += str(block)
                            break

                        else:

                            tt += 1

                    except:

                        tt += 1

                if tt == 3:

                    c = 0

                    for i in [0,2,4]:
                    
                        if int(board[i]) in corners:

                            cc = i
                            c += 1

                    if c == 2:

                        mids.remove(recent)
                        mids.remove(int(board[3]))
                        midsleft = mids.copy()
                        mids.append(recent)
                        mids.append(int(board[3]))

                        block = choice(midsleft)
                        board += str(block)

                    else:

                        block = opposite[str(win2[board[cc] + board[3]])]
                        board += str(block)

        elif tno == 6:

            board += str(recent)

            xx = 0

            for i in [0,2,4]:

                try:

                    if i == 4:

                        k = 0

                    else:

                        k = i + 2

                    if str(win2[board[i] + board[k]]) not in board:

                        block = win2[board[i] + board[k]]
                        board += str(block)
                        break

                    else:

                        xx += 1

                except:

                    xx += 1

            if xx == 3:

                xx = 0
                xxx = 0

                for i in [1,3,5]:

                    try:

                        if i == 5:

                            k = 1

                        else:

                            k = i + 2

                        if str(win2[board[i] + board[k]]) not in board:

                            block = win2[board[i] + board[k]]
                            board += str(block)
                            break

                        else:

                            xx += 1
                            
                            if int(board[i]) in corners:

                                xxx += 1

                    except:

                        xx += 1

                        if int(board[i]) in corners:

                            xxx += 1

                if xx == 3:

                    if xxx == 2:

                        mids.remove(recent)
                        mids.remove(int(board[4]))
                        midsleft = mids.copy()
                        mids.append(recent)
                        mids.append(int(board[4]))

                        block = choice(midsleft)
                        board += str(block)

                    else:

                        for i in corners:

                            if str(i) not in board:

                                movesss = [i]

                        movesss.append(win2[board[4] + str(recent)])

                        block = choice(movesss)
                        board += str(block)

        elif tno == 7:

            board += str(recent)

            ttt = 0

            for i in [1,3,5]:

                try:

                    if i == 5:

                        k = 1

                    else:

                        k = i + 2

                    if str(win2[board[i] + board[k]]) not in board:

                        block = win2[board[i] + board[k]]
                        board += str(block)
                        break

                    else:

                        ttt += 1

                except:

                    ttt += 1

            if ttt == 3:

                ttt = 0

                for i in [0,2,4,6,0,2]:

                    try:

                        if i == 6:

                            k = 0

                        elif ttt > 3:

                            k = i + 4

                        else:

                            k = i + 2

                        if str(win2[board[i] + board[k]]) not in board:

                            block = win2[board[i] + board[k]]
                            board += str(block)
                            break

                        else:

                            ttt += 1

                    except:

                        ttt += 1

                if ttt == 6:

                    movess = []

                    for i in range(9):

                        if str(i) in board:

                            continue

                        else:

                            movess.append(i)

                    block = choice(movess)
                    board += str(block)

        elif tno == 8:

            board += str(recent)

            for i in range(9):

                if str(i) not in board:

                    block = i
                    board += str(block)
                    break

        try:
            
            if tno%2 == 0:
                 
                turtles[tno].shape("X.gif")
                boardspace[block] = True
                
            else:
                
                turtles[tno].shape("O.gif")
                boardspace[block] = False

            turtles[tno].goto(xnodict[str(block)])
            turtles[tno].st()

        except:
            
            pass

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

    global tno, boardspace, playerturn, recent, board

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
            sleep(0.25)
            comp()
    else:
        if tno%2 == 0:
            sleep(0.25)
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
