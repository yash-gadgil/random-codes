'''
from turtle import *
from math import *
from os import *

chdir(getcwd())

class Drawer(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.pensize(5)

    def squares(self):
        
        for i in range(4):
            width = 350
            if i == 0:
                continue
            elif i == 1:
                self.setx(self.xcor() + 800)
            elif i == 2:
                self.sety(self.ycor() + 800)
            else:
                self.setx(self.xcor() - 800)
            self.lt(90)
            for k in range(7):
                self.circle(width * sqrt(2),360,4)
                width -= 50

    def scolors(self):

        for k in range(4):
            self.begin_fill()
            for j in range(4):
                for i in range(3):
                    self.rt(90)
                    self.fd(100)
                for i in range(3):
                    self.fd(100)
                    self.lt(90)
            self.end_fill()
            if k<3:
                self.lt(90)
                self.fd(200)
                self.rt(90)
                self.fd(800)

    def coordinates(self):
        numcoordinates = ["1","2","3","4","5","6","7","8"]
        alphcoordinates = ["a","b","c","d","e","f","g","h",]

        y=-402.5
        for ncoordinate in numcoordinates:
            self.penup()
            self.goto(-428,y)
            self.pendown()
            self.write(ncoordinate, font=("Arial",16,"bold"))
            y+=100
        x=-393
        for acoordinate in alphcoordinates:
            self.penup()
            self.goto(x,-435)
            self.pendown()
            self.write(acoordinate, font=("Arial",16,"bold"))
            x+=100

    def board(self):

        self.penup()
        self.goto(-400,-400)
        self.pendown()

        self.fillcolor("white")
        self.rt(45)
        self.begin_fill()
        self.circle(400 * sqrt(2),360,4)
        self.end_fill()

        self.pensize(3)
        self.squares()
        
        self.lt(45)
        self.fd(800)
        self.setx(self.xcor() + 100)
        self.fillcolor("#51361a")
        self.scolors()

        self.color("white")
        self.coordinates()
        self.ht()

class WPawn():

    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.pensize(5)
'''
'''
def setup(board,white_playing,piece_holder):

    if white_playing:
        b_row = 1,0,3,4
    else:
        b_row = 6,7,4,3
    for i in pieceshapes:
        
        piece_holder[i] = Piece(board,i)
        if i[1] == "K":
            board[b_row[1]][b_row[3]] = i
        elif i[1] == "Q":
            board[b_row[1]][b_row[2]] = i
        else:
            board[b_row[0]][ord(i[2] - 97)] = i
            
    locals().update(piece_holder)
''' 
'''
class pawn(Turtle):

    def __init__(self,color):
        Turtle.__init__(self)

        self.color = color

        self.speed(0)
        self.pu()

        if color == "w":

            pass

        else:
            self.shape("bp.gif")

    def moveset(self,board):

        ind = ind2d(board,piece_name)
        print(ind)
'''
'''
                if r_column[xi] == "0":
                    moves_av.append((xi,ind[1]))
                elif r_column[xi][0] == opp[self.name[0]]:
                    move = xi,ind[1]
                    if passed:
                        moves_av.append(move)
                        break
'''
'''
def setup(board,white_playing,piece_holder):

    if white_playing:
        b_row = 1,0,3,4
    else:
        b_row = 6,7,4,3
    for i in pieceshapes:

        if i == "bp":
            for k in range(8):
                piece_holder["bp" + chr(97 + k)] = Piece(board,"bp" + chr(97 + k))
                board[b_row[0]][k] = "bp" + chr(97 + k)
        elif i == "br":
            for k in "a","h":
                piece_holder["br" + k] = Turtle()
                board[b_row[1]][ord(k) - 97] = "br" + k
        elif i == "bk":
            for k in "b","g":
                piece_holder["bk" + k] = Turtle()
                board[b_row[1]][ord(k) - 97] = "bk" + k
        elif i == "bb":
            for k in "c","f":
                piece_holder["bb" + k] = Turtle()
                board[b_row[1]][ord(k) - 97] = "bb" + k
        elif i == "bq":
            piece_holder["bQ"] = Turtle()
            board[b_row[1]][b_row[2]] = "bQ"
        else:
            piece_holder["bK"] = Turtle()
            board[b_row[1]][b_row[3]] = "bK"
            
    locals().update(piece_holder)
'''
'''
def adjacents(li,index): ########################

    xin, yin = index
    adjacents

    for xi in -1,0,1 :
        for yi in -1,0,1 :
            try:
                li[xin + xi]
'''
'''    
            for yi in range(len(r_row)):
                if r_row[yi] == "0":
                    moves_av.append((ind[0],yi))
'''
'''
(-2,(-1,1)),(2,(-1,1)),((-1,1),2),((-1,1),-2)
'''
'''
            ind = ind2d(board,self.name)
            r_column = [row[ind[1]] for row in board]
            r_row = board[ind[0]]
            moves_av, move_spots, b_store = [], [], []

            for ki in r_column,r_row:
                for xi in range(len(ki)):
                    if ki == r_column:
                        index = xi,ind[1]
                    else:
                        index = ind[0],xi
                    if ki[xi] == "0":
                        b_store.append(index)
                    else:
                        if ki[xi][0] == opp[self.name[0]]:
                            b_store.append(index)
                            move_spots.append(b_store)
                            b_store = [index]
                        elif ki[xi] == self.name:
                            b_store.append(ind)
                        else:
                            move_spots.append(b_store)
                            b_store = []
                else:
                    move_spots.append(b_store)
                    b_store = []

                    for zi in move_spots:
                        if ind in zi:
                            zi.remove(ind)
                            moves_av += zi
                            break
                        
            move_spots, b_store = [], []

            b_column = get_backward_diagonals(gridder(board))
            b_row = get_forward_diagonals(gridder(board))
            diags = []

            for k in b_column,b_row:
                for i in k:
                    if ind in i:
                        diags.append(i)
                        break
            for ki in diags:
                for xi in ki:

                    if board[xi[0]][xi[1]] == "0":
                        b_store.append(xi)
                    else:
                        if board[xi[0]][xi[1]][0] == opp[self.name[0]]:
                            b_store.append(xi)
                            move_spots.append(b_store)
                            b_store = [xi]
                        elif board[xi[0]][xi[1]] == self.name:
                            b_store.append(ind)
                        else:
                            move_spots.append(b_store)
                            b_store = []
                else:
                    move_spots.append(b_store)
                    b_store = []

                    for zi in move_spots:
                        if ind in zi:
                            zi.remove(ind)
                            moves_av += zi
                            break
            
            return moves_av
'''

m = []

if m != []:
    if m[-1] == 0:
        print(0)
