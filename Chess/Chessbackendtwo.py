from turtle import *
from math import *
from os import *
from time import *

pieceshapes = "pawn","rook","king","bishop","horse","queen"
pieces = "bRa","bRh","bNb","bNg","bBc","bBf","bK","bQ"
for i in range(8):
    pieces += ("bp" + chr(97+i),)
board_squares = {}

for l in range(8):
    for j in range(8):
        board_squares[(l, j)] = (-350 + j*100, 350 - l*100)

opp = {"w" : "b", "b" : "w"}
pieces_alive = list(pieces)

moves_played = []  ###

########################################################

def setup(board,white_playing,piece_holder):

    if white_playing:
        b_row = 1,0,3,4
    else:
        b_row = 6,7,4,3
    for i in pieces:
        piece_holder[i] = Piece(board,i)
        if i[1] == "K":
            xi,yi = b_row[1], b_row[3]
        elif i[1] == "Q":
            xi,yi = b_row[1], b_row[2]
        elif i[1] == "p":
            xi,yi = b_row[0], (ord(i[2]) - 97)
        else:
            xi,yi = b_row[1], (ord(i[2]) - 97)
           
        if i == "bpf":
            board[3][4] = i
        else:
            board[xi][yi] = i
        piece_holder[i].p.goto(board_squares[(xi, yi)])
            
    locals().update(piece_holder)
    
########################################################

def gridder(board):
    return [[(i,colno) for colno in range(len(rowno))] for i,rowno in enumerate(board)]

def get_rows(grid):
    return [[c for c in r] for r in grid]

def get_cols(grid):
    return zip(*grid)

def get_backward_diagonals(grid):
    b = [None] * (len(grid) - 1)
    grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
    return [[c for c in r if c is not None] for r in get_cols(grid)]

def get_forward_diagonals(grid):
    b = [None] * (len(grid) - 1)
    grid = [b[:i] + r + b[i:] for i, r in enumerate(get_rows(grid))]
    return [[c for c in r if c is not None] for r in get_cols(grid)]


def ind2d(li,ele):
    for i,k in enumerate(li):
        if ele in k:
            return (i, k.index(ele))

class Drawer(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.pensize(5)

    def go(self,xc,yc):

        self.pu()
        self.goto(xc,yc)
        self.pd()

    def squares(self):
        
        for i in range(1,4):
            width = 350
            if i == 1:
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
        numcoordinates = "1","2","3","4","5","6","7","8"
        alphcoordinates = "a","b","c","d","e","f","g","h"

        y = -402.5
        for ncoordinate in numcoordinates:
            self.go(-428,y)
            self.write(ncoordinate, font=("Arial",16,"bold"))
            y+=100
        x = -393
        for acoordinate in alphcoordinates:
            self.go(x,-435)
            self.write(acoordinate, font=("Arial",16,"bold"))
            x+=100

    def board(self):

        self.go(-400,-400)

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

        self.go(-400,-400)
        self.lt(45)
        self.squares()

        self.color("white")
        self.coordinates()
        self.ht()
        
class CScreen(TurtleScreen):

    def __init__(self):
        
        self = Screen()
        self.delay(0)

        title("Chess")
        bgcolor("#C19A6B")
        #print(type(self))
        
        chdir(getcwd())

        for color in "black","white":
            for piece in pieceshapes:
                self.register_shape(color + piece + ".gif")
      
class Piece():

    def __init__(self,board,name):
        
        self.board = board
        self.name = name

        if self.name[1] == "p":

            self.p = self.pawn(self.name)

        elif self.name[1] == "R":

            self.p = self.rook(self.name)
            
        elif self.name[1] == "N":

            self.p = self.knight(self.name)

        elif self.name[1] == "B":

            self.p = self.bishop(self.name)

        elif self.name[1] == "Q":

            self.p = self.queen(self.name)

        elif self.name[1] == "K":

            self.p = self.king(self.name)

        self.p.speed(0)
        self.p.pu()

    class pawn(Turtle): #en passant needed

        def __init__(self,name):
            Turtle.__init__(self)
            self.name = name

            if name[0] == "w":
                self.shape("whitepawn.gif")
            else:
                self.shape("blackpawn.gif")

        def moveset(self,board,w_pl):

            ind, moves_av = ind2d(board,self.name), []

            if (w_pl and self.name[0] == "w") or (not w_pl and self.name[0] == "b"):
                hi = -1
            elif (not w_pl and self.name[0] == "w") or (w_pl and self.name[0] == "b"):
                hi = 1

            if ind[0] == 1 or ind[0] == 6:
                try:
                    if board[ind[0] + 2*hi][ind[1]] == "0":
                        moves_av.append((ind[0] + 2*hi, ind[1]))
                except:
                    pass
            if board[ind[0] + hi][ind[1]] == "0":
                moves_av.append((ind[0] + hi, ind[1]))
            for ki in -1,1:
                if board[ind[0] + hi][ind[1] + ki][0] == opp[self.name[0]]: #side pawns error?
                    moves_av.append((ind[0] + hi, ind[1] + ki))
            if moves_played != []:  #check code below
                if (moves_played[-1][2][:2] == (opp[self.name[0]] + "p")) and ((moves_played[-1][1][0] - moves_played[-1][0][0])%2 == 0) and ((moves_played[-1][1][1] == (ind[1] + 1)) or (moves_played[-1][1][1] == (ind[1] - 1))):
                    moves_av.append((ind[0] + hi, moves_played[-1][1][1]))

            return moves_av

    class rook(Turtle):

        def __init__(self,name):
            Turtle.__init__(self) #self.name[0]
            self.name = name

            if name[0] == "w":

                self.shape("whiterook.gif")

            else:
                self.shape("blackrook.gif")

        def moveset(self,board,w_pl):

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

            return moves_av

    class knight(Turtle):

        def __init__(self,name):
            Turtle.__init__(self)
            self.name = name

            if name[0] == "w":

                self.shape("whitehorse.gif")

            else:
                self.shape("blackhorse.gif")

        def moveset(self,board,w_pl):

            ind, moves_av = ind2d(board,self.name), []

            for i in ((-2,2),(-1,1)),((-1,1),(-2,2)):
                for xi in i[0]:
                    for yi in i[1]:
                        try:
                            if board[ind[0] + xi][ind[1] + yi][0] == self.name[0]:
                                continue
                            else:
                                moves_av.append((ind[0] + xi,ind[1] + yi))
                        except:
                            continue
            return moves_av

    class bishop(Turtle):

        def __init__(self,name):
            Turtle.__init__(self)
            self.name = name

            if name[0] == "w":

                self.shape("whitebishop.gif")

            else:
                self.shape("blackbishop.gif")

        def moveset(self,board,w_pl):

            ind = ind2d(board,self.name)

            r_column = get_backward_diagonals(gridder(board))
            r_row = get_forward_diagonals(gridder(board))
            diags = []

            for k in r_column,r_row:
                for i in k:
                    if ind in i:
                        diags.append(i)
                        break

            moves_av, move_spots, b_store = [], [], []

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

    class queen(Turtle):

        def __init__(self,name):
            Turtle.__init__(self)
            self.name = name

            if name[0] == "w":

                self.shape("whitequeen.gif")

            else:
                self.shape("blackqueen.gif")

        def moveset(self,board,w_pl):

            ind = ind2d(board,self.name)
            r_column = [row[ind[1]] for row in gridder(board)]
            r_row = gridder(board)[ind[0]]
            b_column = get_backward_diagonals(gridder(board))
            b_row = get_forward_diagonals(gridder(board))
            moves_av, move_spots, b_store, diags = [], [], [], []
            for k in b_column,b_row:
                for i in k:
                    if ind in i:
                        diags.append(i)
                        break
                        
            for ki in diags[0],diags[1],r_column,r_row:
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

    class king(Turtle):

        def __init__(self,name):
            Turtle.__init__(self)
            self.name = name
            
            if name[0] == "w":
                self.shape("whiteking.gif")

            else:
                self.shape("blackking.gif")

        def moveset(self,board):

            ind = ind2d(board,self.name)

            moves_av = []

            for xi in -1,0,1:
                for yi in -1,0,1:
                    if board[ind[0] + xi][ind[1] + yi] == "0":

                        pass
            
