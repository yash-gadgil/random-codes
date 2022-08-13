

import turtle
import os

'''
def boardsetup():
    
    
    s=turtle.getscreen()
    turtle.title("Chess")
    turtle.bgcolor("#C19A6B")
    t=turtle.Turtle()
    turtle.ht()
    t.speed(0)
    t.pensize(3)
    
    t.penup()
    t.goto(-400,-400)
    t.pendown()
    
    #boardframe
    t.pensize(5)
    t.fillcolor("white")
    t.begin_fill()
    t.fd(800)
    t.lt(90)
    t.fd(800)
    t.lt(90)
    t.fd(800)
    t.lt(90)
    t.fd(800)
    t.end_fill()
    t.pensize(3)
    
    #squares
    t.fillcolor("black")
    t.bk(100)
    t.lt(90)
    t.fd(800)
    for i in range(3):
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(800)
        t.rt(90)
        t.fd(100)
        t.rt(90)
        t.fd(800)

    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)

    for i in range(3):
        t.lt(90)
        t.fd(800)
        t.rt(90)
        t.fd(100)
        t.rt(90)
        t.fd(800)
        t.lt(90)
        t.fd(100)

    t.lt(90)
    t.fd(800)

    for k in range(4):
        
        t.begin_fill()
        for j in range(4):
            for i in range(3):
                t.rt(90)
                t.fd(100)
            for i in range(3):
                t.fd(100)
                t.lt(90)
        t.end_fill()
        if k<3:
            t.lt(90)
            t.fd(200)
            t.rt(90)
            t.fd(800)


    #coordinates

    numcoordinates = ["1","2","3","4","5","6","7","8"]
    alphcoordinates = ["a","b","c","d","e","f","g","h",]
    t.color("white")
    y=-402.5
    for ncoordinate in numcoordinates:
        t.penup()
        t.goto(-428,y)
        t.pendown()
        t.write(ncoordinate, font=("Arial",16,"bold"))
        y+=100
    x=-393
    for acoordinate in alphcoordinates:
        t.penup()
        t.goto(x,-435)
        t.pendown()
        t.write(acoordinate, font=("Arial",16,"bold"))
        x+=100

    t.ht()
'''   
    
    
    

def pieces():
    os.chdir("C:\\Users\\Dell\\Downloads")
    
    #piece graphics
    
    s.register_shape("whitepawn1.gif")
    s.register_shape("whiterook1.gif")
    s.register_shape("whiteknight1.gif")
    s.register_shape("whitebishop.gif")
    s.register_shape("whitequeennew.gif")
    s.register_shape("whiteking1.gif")
    
    s.register_shape("blackpawn1.gif")
    s.register_shape("blackrook111.gif")
    s.register_shape("blackknight11.gif")
    
    
    
    a2 = turtle.Turtle()
    a2.shape("whitepawn1.gif")
    a2.speed(6)
    a2.penup()
    a2.goto(-350,-250)
    
    b2 = turtle.Turtle()
    b2.shape("whitepawn1.gif")
    b2.speed(6)
    b2.penup()
    b2.goto(-250,-250)
    
    c2 = turtle.Turtle()
    c2.shape("whitepawn1.gif")
    c2.speed(6)
    c2.penup()
    c2.goto(-150,-250)
    
    d2 = turtle.Turtle()
    d2.shape("whitepawn1.gif")
    d2.speed(6)
    d2.penup()
    d2.goto(-50,-250)
    
    e2 = turtle.Turtle()
    e2.shape("whitepawn1.gif")
    e2.speed(6)
    e2.penup()
    e2.goto(50,-250)
    
    f2 = turtle.Turtle()
    f2.shape("whitepawn1.gif")
    f2.speed(6)
    f2.penup()
    f2.goto(150,-250)
    
    g2 = turtle.Turtle()
    g2.shape("whitepawn1.gif")
    g2.speed(6)
    g2.penup()
    g2.goto(250,-250)
    
    h2 = turtle.Turtle()
    h2.shape("whitepawn1.gif")
    h2.speed(6)
    h2.penup()
    h2.goto(350,-250)


g = ["a2","b2","c2","d2","e2","f2","g2","h2","wRa","wRh","wNb","wNg","wBc","wBf","wK","wQ","a7","b7","c7","d7","e7","f7","g7","h7",]






def dragginga2(xa2,ya2):
    a2.ondrag(None)
    a2.penup()
    a2.goto(xa2,ya2)
    a2.pendown()
    a2.ondrag(dragginga2)
    
def draggingb2(xb2,yb2):
    b2.ondrag(None)
    b2.penup()
    b2.goto(xb2,yb2)
    b2.pendown()
    b2.ondrag(draggingb2)

def draggingc2(xc2,yc2):
    c2.ondrag(None)
    c2.penup()
    c2.goto(xc2,yc2)
    c2.pendown()
    c2.ondrag(draggingc2)
    
def draggingd2(xd2,yd2):
    d2.ondrag(None)
    d2.penup()
    d2.goto(xd2,yd2)
    d2.pendown()
    d2.ondrag(draggingd2)
    
def dragginge2(xe2,ye2):
    e2.ondrag(None)
    e2.penup()
    e2.goto(xe2,ye2)
    e2.pendown()
    e2.ondrag(dragginge2)    
    
def draggingf2(xf2,yf2):
    f2.ondrag(None)
    f2.penup()
    f2.goto(xf2,yf2)
    f2.pendown()
    f2.ondrag(draggingf2)
    
def draggingg2(xg2,yg2):
    g2.ondrag(None)
    g2.penup()
    g2.goto(xg2,yg2)
    g2.pendown()
    g2.ondrag(draggingg2)
    
def draggingh2(xh2,yh2):
    h2.ondrag(None)
    h2.penup()
    h2.goto(xh2,yh2)
    h2.pendown()
    h2.ondrag(draggingh2)
    
def draggingwK(xwK,ywK):
    wK.ondrag(None)
    wK.penup()
    wK.goto(xwK,ywK)
    wK.pendown()
    wK.ondrag(draggingwK)
     
def draggingwQ(xwQ,ywQ):
    wQ.ondrag(None)
    wQ.penup()
    wQ.goto(xwQ,ywQ)
    wQ.pendown()
    wQ.ondrag(draggingwQ)
    

    
    
'''
#pieces

os.chdir("C:\\Users\\Dell\\Downloads")

###
#whitepieces
###


#whitepawns
        
whitepawns = ["a2","b2","c2","d2","e2","f2","g2","h2"]
s.register_shape("whitepawn1.gif")#

x=-350
for pawn in whitepawns:
    pawn = turtle.Turtle()
    pawn.shape("whitepawn1.gif")
    pawn.speed(5)
    pawn.penup()
    pawn.goto(x,-250)
    x+=100
    
  
#whiterooks

whiterooks = ["wRa","wRh"]
s.register_shape("whiterook1.gif")#

x=-350
for rook in whiterooks:
    rook = turtle.Turtle()
    rook.shape("whiterook1.gif")
    rook.speed(5)
    rook.penup()
    rook.goto(x,-350)
    x+=700


#white knights
    
whiteknights = ["wNb","wNg"]
s.register_shape("whiteknight1.gif")#

x=-250
for knight in whiteknights:
    knight = turtle.Turtle()
    knight.shape("whiteknight1.gif")
    knight.speed(5)
    knight.penup()
    knight.goto(x,-350)
    x+=500

#white bishops
    
whitebishops = ["wBc","wBf"]
s.register_shape("whitebishop.gif")#

x=-150
for bishop in whitebishops:
    bishop = turtle.Turtle()
    bishop.shape("whitebishop.gif")
    bishop.speed(5)
    bishop.penup()
    bishop.goto(x,-350)
    x+=300

#white queen and king
    
s.register_shape("whitequeennew.gif")#

wQ = turtle.Turtle()
wQ.shape("whitequeennew.gif")
wQ.speed(5)
wQ.penup()
wQ.goto(-50,-350)

s.register_shape("whiteking1.gif")#

wK = turtle.Turtle()
wK.shape("whiteking1.gif")
wK.speed(5)
wK.penup()
wK.goto(50,-350)



###
#black pieces
###


#blackpawns
        
blackpawns = ["a7","b7","c7","d7","e7","f7","g7","h7"]
s.register_shape("blackpawn1.gif")#

x=-350
for bpawn in blackpawns:
    bpawn = turtle.Turtle()
    bpawn.shape("blackpawn1.gif")
    bpawn.speed(5)
    bpawn.penup()
    bpawn.goto(x,250)
    x+=100


#black rooks
    
blackrooks = ["bRa","bRh"]
s.register_shape("blackrook111.gif")

x=-350
for brook in blackrooks:
    brook = turtle.Turtle()
    brook.shape("blackrook111.gif")
    brook.speed(5)
    brook.penup()
    brook.goto(x,350)
    x+=700


#black knights
    
blackknights = ["bNb","bNg"]
s.register_shape("blackknight11.gif")

x=-250
for bknight in blackknights:
    bknight = turtle.Turtle()
    bknight.shape("blackknight11.gif")
    bknight.speed(5)
    bknight.penup()
    bknight.goto(x,350)
    x+=500
'''