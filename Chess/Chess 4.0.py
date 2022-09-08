
# main problems:
# king can't take queen when in check
# no checking system
# no checkmate
# no en passant
# no castling
# no pinning of pieces
# discovered attacks
# turn based
# change coordinates for black


from turtle import *
from os import *
from math import *
from random import *
import traceback

chdir(getcwd())

s = Screen()
bgcolor("#C19A6B")
s.delay(0)

s.register_shape("startbp.gif")
s.register_shape("startbup.gif")
s.register_shape("exitebp.gif")
s.register_shape("exitebup.gif")
s.register_shape("whitechoicebp.gif")
s.register_shape("whitechoicebup.gif") 
s.register_shape("blackchoicebp.gif")
s.register_shape("blackchoicebup.gif")
s.register_shape("highlighter.gif")
#pieceshapes = "pawn","rook","king","bishop","horse","queen"
for i in "white","black":
    for k in "pawn","rook","king","bishop","knight","queen":
        s.register_shape(i + k + ".gif")

opp_color = {"black" : "white", "white" : "black"}
all_pieces = []

selected = None
check = 0

index_coord = {}
'''
for i in range(8):
    yc = (4 - i) * 87.5 if i < 4 else (3 - i) * 87.5
    for k in range(8):
        xc = (k - 4) * 87.5 if k < 4 else (k - 3) * 87.5
        index_coord[(k,i)] = (xc,yc)
print(index_coord)
'''

highlighters = []
shown_highlighters = []


for l in range(8):
    for j in range(8):
        index_coord[(j, l)] = (-350 + j*100, 350 - l*100) # tile,row -> j,l

#print(index_coord[(1,0)])

#print(index_coord)
#t = Turtle()
#t.goto(index_coord[(0,0)])

# Drawer #


def set_pieces(board): ###############

    if white_playing:
        setting = [1, 6, 0, 7] # setting[0] is row for black pawns [1] for white pawns [2] for black special pieces [3] for white special pieces
    else:
        setting = [6, 1, 7, 0]

    for a,row in enumerate(setting):
        
        for i in range(8):

            col = "black" if a%2 == 0 else "white"
            
            if row in (1,6):       
                board[row][i].Occupy(Pawn(col))
            else:
                if i in (0,7):
                    board[row][i].Occupy(Rook(col))
                elif i in (1,6):
                    board[row][i].Occupy(Knight(col))
                elif i in (2,5):
                    board[row][i].Occupy(Bishop(col))
                elif i == 3:
                    if white_playing:
                        board[row][i].Occupy(Queen(col))
                    else:
                        board[row][i].Occupy(King(col))
                else:
                    if white_playing:
                        board[row][i].Occupy(King(col))
                    else:
                        board[row][i].Occupy(Queen(col))
                        
            board[row][i].Occupant.goto( index_coord[ i,row ] )
            


class Drawer(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.pensize(5)
        self.ht()
        #drawers.append(self)

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

    def board(self): # needs refining

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

        self.color("black")
        self.coordinates()
        self.ht()
        self.pu()
        self.home()
        self.pd()

class Tile(): #Turtle
    

    def __init__(self,Occupant = 0): # add Color #self.Color = Color
        #Turtle.__init__(self)
        self.Occupant = Occupant

    def Occupied(self):
        return self.Occupant != 0

    def Attackable(self,PieceColor):
        return self.Occupant.color == opp_color[PieceColor] if self.Occupied() else 0

    def Movable(self,PieceColor):
        return 1 if self.Occupant == 0 or self.Occupant.color == opp_color[PieceColor] else 0

    def Occupy(self,Occupier):
        self.Occupant = Occupier

    def Identify(self,Piece):
        return self.Occupant == Piece
#print(board)


class Pawn(Turtle):

    def __init__(self,color): # color = white or black
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        self.color = color
        self.type = "pawn"
        #self.moves_av = []
        
        if self.color == "white":
            self.shape("whitepawn.gif")
            white_pieces.append(self)
            self.direction = -1 if white_playing else 1
        else:
            self.shape("blackpawn.gif")
            black_pieces.append(self)
            self.direction = 1 if white_playing else -1
            
        self.start = 6 if self.direction == -1 else 1
        
        listen()
        self.onclick(self.p_selected)

    def attack(self):
        attack_moves = []

        for b,row in enumerate(board):
            for a,tile in enumerate(row):
                
                if tile.Identify(self):

                    for i in -1,1:
                        try:
                            if board[b + self.direction][a + i].Attackable(self.color):
                                attack_moves.append((a + i,b + self.direction))
                        except:
                            pass

                    return attack_moves
                            

    def moveset(self):
        moves_av = []

        for b,row in enumerate(board):
            for a,tile in enumerate(row):
                
                if tile.Identify(self):

                    if b == self.start and not board[b + 2 * self.direction][a].Occupied() and not board[b + self.direction][a].Occupied():
                        moves_av.append((a,b + 2 * self.direction))
                    if not board[b + self.direction][a].Occupied():
                        moves_av.append((a,b + self.direction))
                    for i in -1,1:
                        try:
                            if board[b + self.direction][a + i].Attackable(self.color):
                                moves_av.append((a + i,b + self.direction))
                        except:
                            pass

                    return moves_av

    def p_selected(self,x,y):
        global selected, shown_highlighters

        if (self.color == "white" and turn) or (self.color == "black" and not turn):
            selected = self
            moves = self.moveset()

            for highlight in shown_highlighters:
                highlight.ht()
            shown_highlighters = []
            
            for move in moves:
                for highlight in highlighters:
                    if move == highlight.coord:
                        highlight.st()
                        shown_highlighters.append(highlight)

        
                        
class Rook(Turtle):
                
    def __init__(self,color):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        self.color = color
        self.moved = 0
        self.type = "rook"
        #self.moves_av = []
        
        if self.color == "white":
            self.shape("whiterook.gif")
            white_pieces.append(self)
        else:
            self.shape("blackrook.gif")
            black_pieces.append(self)

        listen()
        self.onclick(self.p_selected)

    def moveset(self):
        moves_av = []

        for b,row in enumerate(board):
            for a,tile in enumerate(row):

                if tile.Identify(self): ## make smaller ## 

                    column = [row[a] for row in board]

                    
                    for line in row[a + 1:], row[:a][::-1]:
                        for tile1 in line:
                            if tile1.Movable(self.color):
                                moves_av.append((row.index(tile1),b))
                                if not tile1.Occupied:
                                    continue
                                if tile1.Attackable(self.color):
                                    break
                            else:
                                break

                    for line in column[b + 1:], column[:b][::-1]:
                        for tile1 in line:
                            if tile1.Movable(self.color):
                                moves_av.append((a,column.index(tile1)))
                                if not tile1.Occupied:
                                    continue
                                if tile1.Attackable(self.color):
                                    break
                            else:
                                break
                    '''
                    for tile1 in row[:a][::-1]:
                        if tile1.Movable(self.color):
                            moves_av.append((row.index(tile1),b))
                            if tile1.Attackable(self.color):
                                break
                        else:
                            break
                    

                    for tile1 in column[b + 1:]:
                        if tile1.Movable(self.color):
                            moves_av.append((a,column.index(tile1)))
                            if tile1.Attackable(self.color):
                                break
                        else:
                            break

                    for tile1 in column[:b][::-1]:
                        if tile1.Movable(self.color):
                            moves_av.append((a,column.index(tile1)))
                            if tile1.Attackable(self.color):
                                break
                        else:
                            break
                    '''
                        
                    return moves_av
                
    def p_selected(self,x,y):
        global selected, shown_highlighters
        
        if (self.color == "white" and turn) or (self.color == "black" and not turn):
            selected = self
            moves = self.moveset()

            for highlight in shown_highlighters:
                highlight.ht()
            shown_highlighters = []
            
            for move in moves:
                for highlight in highlighters:
                    if move == highlight.coord:
                        highlight.st()
                        shown_highlighters.append(highlight)

class Bishop(Turtle):

    def __init__(self,color):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        self.color = color
        self.type = "bishop"

        if self.color == "white":
            self.shape("whitebishop.gif")
            white_pieces.append(self)
        else:
            self.shape("blackbishop.gif")
            black_pieces.append(self)

        listen()
        self.onclick(self.p_selected)

    def moveset(self):
        moves_av = []

        for b,row in enumerate(board):
            for a,tile in enumerate(row):

                if tile.Identify(self):

                    for i in (-1,-1),(-1,1),(1,-1),(1,1):
                        for k in range(1,8):
                            try:
                                tile1 = board[b + k*i[1]][a + k*i[0]]
                                if tile1.Movable(self.color):
                                    moves_av.append((a + k*i[0],b + k*i[1]))
                                    if not tile1.Occupied:
                                        continue
                                    if tile1.Attackable(self.color):
                                        break
                                else:
                                    break
                            except:
                                break
                            
                    return moves_av
                
    def p_selected(self,x,y):
        global selected, shown_highlighters

        if (self.color == "white" and turn) or (self.color == "black" and not turn):
            selected = self
            moves = self.moveset()

            for highlight in shown_highlighters:
                highlight.ht()
            shown_highlighters = []
            
            for move in moves:
                for highlight in highlighters:
                    if move == highlight.coord:
                        highlight.st()
                        shown_highlighters.append(highlight)
            
class Knight(Turtle):

    def __init__(self,color):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        self.color = color
        self.type = "knight"

        if self.color == "white":
            self.shape("whiteknight.gif")
            white_pieces.append(self)
        else:
            self.shape("blackknight.gif")
            black_pieces.append(self)

        listen()
        self.onclick(self.p_selected)

    def moveset(self):
        moves_av = []

        for b,row in enumerate(board):
            for a,tile in enumerate(row):

                if tile.Identify(self):

                    for i in (-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2):
                        try:
                            tile1 = board[b + i[1]][a + i[0]]
                            if tile1.Movable(self.color):
                                moves_av.append((a + i[0],b + i[1]))
                        except:
                            pass
                            
                    return moves_av

    def p_selected(self,x,y):
        global selected, shown_highlighters

        if (self.color == "white" and turn) or (self.color == "black" and not turn):
            selected = self
            moves = self.moveset()

            for highlight in shown_highlighters:
                highlight.ht()
            shown_highlighters = []
            
            for move in moves:
                for highlight in highlighters:
                    if move == highlight.coord:
                        highlight.st()
                        shown_highlighters.append(highlight)

class Queen(Turtle):

    def __init__(self,color):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        self.color = color
        self.type = "queen"

        if self.color == "white":
            self.shape("whitequeen.gif")
            white_pieces.append(self)
        else:
            self.shape("blackqueen.gif")
            black_pieces.append(self)

        listen()
        self.onclick(self.p_selected)

    def moveset(self):
        moves_av = []

        for b,row in enumerate(board):
            for a,tile in enumerate(row):

                if tile.Identify(self):

                    for i in (-1,-1),(-1,1),(1,-1),(1,1):
                        for k in range(1,8):
                            try:
                                tile1 = board[b + k*i[1]][a + k*i[0]]
                                if tile1.Movable(self.color):
                                    moves_av.append((a + k*i[0],b + k*i[1]))
                                    if not tile1.Occupied:
                                        continue
                                    if tile1.Attackable(self.color):
                                        break
                                else:
                                    break
                            except:
                                break

                    column = [row[a] for row in board]
                    
                    for line in row[a + 1:], row[:a][::-1]:
                        for tile1 in line:
                            if tile1.Movable(self.color):
                                moves_av.append((row.index(tile1),b))
                                if not tile1.Occupied:
                                    continue
                                if tile1.Attackable(self.color):
                                    break
                            else:
                                break

                    for line in column[b + 1:], column[:b][::-1]:
                        for tile1 in line:
                            if tile1.Movable(self.color):
                                moves_av.append((a,column.index(tile1)))
                                if not tile1.Occupied:
                                    continue
                                if tile1.Attackable(self.color):
                                    break
                            else:
                                break
                            
                    return moves_av
                
    def p_selected(self,x,y):
        global selected, shown_highlighters

        if (self.color == "white" and turn) or (self.color == "black" and not turn):
            selected = self
            moves = self.moveset()

            for highlight in shown_highlighters:
                highlight.ht()
            shown_highlighters = []
            
            for move in moves:
                for highlight in highlighters:
                    if move == highlight.coord:
                        highlight.st()
                        shown_highlighters.append(highlight)

class King(Turtle):

    def __init__(self,color):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        self.color = color
        self.moved = 0
        self.type = "king"

        if self.color == "white":
            self.shape("whiteking.gif")
            white_pieces.append(self)
        else:
            self.shape("blackking.gif")
            black_pieces.append(self)

        listen()
        self.onclick(self.p_selected)

    def influence(self):
        moves_av = []

        for b,row in enumerate(board):
            for a,tile in enumerate(row):

                if tile.Identify(self):

                    for i in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1):

                        try:
                            tile1 = board[b + i[1]][a + i[0]]
                            if tile1.Movable(self.color):
                                moves_av.append((a + i[0],b + i[1]))
                        except:
                            pass
                        
                    return moves_av

    def moveset(self):
        moves_av = []

        opp_pieces = white_pieces if self.color == "black" else black_pieces
        opp_moves = []

        for piece in opp_pieces:

            if piece.type == "pawn" and piece.attack() != None:
                opp_moves.extend(piece.attack())
                #print(piece.attack())
            elif piece.type == "king":
                opp_moves.extend(piece.influence())
            else:
                opp_moves.extend(piece.moveset())

        opp_moves = list(set(opp_moves))

        for b,row in enumerate(board):
            for a,tile in enumerate(row):

                if tile.Identify(self):

                    for i in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1):

                        try:
                            tile1 = board[b + i[1]][a + i[0]]
                            if tile1.Movable(self.color):
                                moves_av.append((a + i[0],b + i[1]))
                        except:
                            pass

        '''
        for move in moves_av:
            if move in opp_moves:
                moves_av.remove(move)
        '''
        moves_av = [move for move in moves_av if move not in opp_moves]

        print(opp_moves)
        print(moves_av)
        print()
        return moves_av

    def p_selected(self,x,y):
        global selected, shown_highlighters

        if (self.color == "white" and turn) or (self.color == "black" and not turn):
            selected = self
            moves = self.moveset()

            for highlight in shown_highlighters:
                highlight.ht()
            shown_highlighters = []
            
            for move in moves:
                for highlight in highlighters:
                    if move == highlight.coord:
                        highlight.st()
                        shown_highlighters.append(highlight)
    
def Choice():
    start.ht()
    whitechoice.st()
    blackchoice.st()

def WhiteChosen():
    global white_playing
    white_playing = 1
    Start()

def BlackChosen():
    global white_playing
    white_playing = 0
    Start()   

def Start():
    global black_pieces, white_pieces, all_pieces, board

    board = [[Tile() for k in range(8)] for i in range(8)]
    
    whitechoice.ht()
    blackchoice.ht()
    #drawers = [Drawer()]
    drawers[0].board()
    exite.st()
    
    black_pieces = []
    white_pieces = []

    set_pieces(board)

    for coord in index_coord:
        highlighters.append(Highlighter())
        highlighters[-1].goto(index_coord[coord])
        highlighters[-1].setcoord(coord)

    all_pieces = white_pieces + black_pieces


class Highlighter(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.shape("highlighter.gif")
        self.pu()
        self.speed(0)
        self.ht()

        listen()
        self.onclick(self.moved)

    def setcoord(self,coord):
        self.coord = coord

    def moved(self,x,y):
        global selected, shown_highlighters, check, turn

        turn = not turn

        for highlight in shown_highlighters:
            highlight.ht()
        shown_highlighters = []

        selected.goto(index_coord[self.coord])
        tile1 = board[self.coord[1]][self.coord[0]]
        if tile1.Occupied:
            try:
                tile1.Occupant.ht()
            except AttributeError:
                pass

        for row in board:
            for tile2 in row:
                if tile2.Occupant == selected:
                    tile2.Occupy(0)
                    tile1.Occupy(selected)

                    '''
                    self_pieces,opp_pieces = (white_pieces,black_pieces) if selected.color == "white" else (black_pieces,white_pieces)
                    self_piece_moves = []
                    for piece in self_pieces:
                        self_piece_moves.extend(piece.moveset())
                    for piece in opp_pieces:
                        if piece.type == "king":
                            for b,row in enumerate(board):
                                for a,tile1 in enumerate(row):
                                    if tile1.Occupant == piece:
                                        if (a,b) in self_piece_moves:
                                            check = 1
                                        selected = None ### need to change check checking
                                        #print(check)
                                        return
                    '''
                    selected = None
                    return
            
        
        #print(tile1.Occupant)
        
        
        

        
# Button #
class Button(Turtle):

    def __init__(self,xb,yb,func, def_name = None):
        Turtle.__init__(self)
        self.xb = xb
        self.yb = yb
        self.func = func

        if def_name == None:
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
        self.defined_name = def_name

        self.shape(self.defined_name + "bup.gif") # starting shape
        self.speed(0)
        self.pu()
        self.goto(xb,yb)

        listen()
        self.onclick(self.OnClick, 1)
        self.onrelease(self.Command, 1)

    def OnClick(self,x,y):
        self.shape(self.defined_name + "bp.gif") # onpress shape

    def Command(self,x,y):
        self.shape(self.defined_name + "bup.gif")
        ontimer(self.func, 50) #40

def menu():
    global all_pieces, shown_highlighters, turn

    for highlight in shown_highlighters:
        highlight.ht()
    shown_highlighters = []

    turn = 1 # 1 for white turn 0 for black turn

    if drawers != []:
        drawers[0].clear()
        exite.ht()
        for piece in all_pieces:
            piece.ht()
            del piece
        all_pieces = []
    start.st()

drawers = [Drawer()]
start = Button(0,0,Choice)
start.ht()
exite = Button(500,-100,menu)
exite.ht()
whitechoice = Button(50,0,WhiteChosen)
blackchoice = Button(-50,0,BlackChosen)
whitechoice.ht()
blackchoice.ht()

menu()
