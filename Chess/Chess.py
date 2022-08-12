import turtle
import os
from time import *


s=turtle.getscreen()
s.delay(0)
turtle.title("Chess")
turtle.bgcolor("#C19A6B")
t=turtle.Turtle()
turtle.ht()
t.speed(0)
t.pensize(3)


t.penup()
t.goto(-400,-400)
t.pendown()

'''
def dragging(xK,yK):
    wK.ondrag(None)
    wK.penup()
    wK.goto(xK,yK)
    wK.pendown
    wK.ondrag(dragging)
    
   
def draggin(xQ,yQ):
    wQ.ondrag(None)
    wQ.penup()
    wQ.goto(xQ,yQ)
    wQ.pendown
    wQ.ondrag(draggin)
'''

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


os.chdir(os.getcwd())

s.register_shape("whitepawn1.gif")
s.register_shape("whitequeennew.gif")
s.register_shape("whiteking1.gif")
s.register_shape("whiterook1.gif")
s.register_shape("whiteknight1.gif")
s.register_shape("whitebishop.gif")

s.register_shape("blackpawn1.gif")
s.register_shape("blackrook111.gif")
s.register_shape("blackknight11.gif")

spd=7

a2 = turtle.Turtle()
a2.shape("whitepawn1.gif")
a2.speed(spd)
a2.penup()
a2.goto(-350,-250)

b2 = turtle.Turtle()
b2.shape("whitepawn1.gif")
b2.speed(spd)
b2.penup()
b2.goto(-250,-250)

c2 = turtle.Turtle()
c2.shape("whitepawn1.gif")
c2.speed(spd)
c2.penup()
c2.goto(-150,-250)

d2 = turtle.Turtle()
d2.shape("whitepawn1.gif")
d2.speed(spd)
d2.penup()
d2.goto(-50,-250)

e2 = turtle.Turtle()
e2.shape("whitepawn1.gif")
e2.speed(spd)
e2.penup()
e2.goto(50,-250)

f2 = turtle.Turtle()
f2.shape("whitepawn1.gif")
f2.speed(spd)
f2.penup()
f2.goto(150,-250)

g2 = turtle.Turtle()
g2.shape("whitepawn1.gif")
g2.speed(spd)
g2.penup()
g2.goto(250,-250)

h2 = turtle.Turtle()
h2.shape("whitepawn1.gif")
h2.speed(spd)
h2.penup()
h2.goto(350,-250)

wRa = turtle.Turtle()
wRa.shape("whiterook1.gif")
wRa.speed(spd)
wRa.penup()
wRa.goto(-350,-350)

wRh = turtle.Turtle()
wRh.shape("whiterook1.gif")
wRh.speed(spd)
wRh.penup()
wRh.goto(350,-350)

wNb = turtle.Turtle()
wNb.shape("whiteknight1.gif")
wNb.speed(spd)
wNb.penup()
wNb.goto(-250,-350)

wNg = turtle.Turtle()
wNg.shape("whiteknight1.gif")
wNg.speed(spd)
wNg.penup()
wNg.goto(250,-350)

wBc = turtle.Turtle()
wBc.shape("whitebishop.gif")
wBc.speed(spd)
wBc.penup()
wBc.goto(-150,-350)

wBf = turtle.Turtle()
wBf.shape("whitebishop.gif")
wBf.speed(spd)
wBf.penup()
wBf.goto(150,-350)

wQ = turtle.Turtle()
wQ.shape("whitequeennew.gif")
wQ.speed(spd)
wQ.penup()
wQ.goto(-50,-350)

wK = turtle.Turtle()
wK.shape("whiteking1.gif")
wK.speed(spd)
wK.penup()
wK.goto(50,-350)

a7 = turtle.Turtle()
a7.shape("blackpawn1.gif")
a7.speed(spd)
a7.penup()
a7.goto(-350,250)



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
r = False
def dragginga2(xa2,ya2):
    global r
    r = True
    a2.ondrag(None)
    a2.penup()
    a2.goto(xa2,ya2)
    a2.ondrag(dragginga2)
    
def draggingb2(xb2,yb2):
    #b2.ondrag(None)
    b2.goto(xb2,yb2)
    #b2.ondrag(draggingb2)

def draggingc2(xc2,yc2):
    c2.ondrag(None)
    c2.penup()
    c2.goto(xc2,yc2)
    c2.ondrag(draggingc2)
    
def draggingd2(xd2,yd2):
    d2.ondrag(None)
    d2.penup()
    d2.goto(xd2,yd2)
    d2.ondrag(draggingd2)
    
def dragginge2(xe2,ye2):
    e2.ondrag(None)
    e2.penup()
    e2.goto(xe2,ye2)
    e2.ondrag(dragginge2)    
    
def draggingf2(xf2,yf2):
    f2.ondrag(None)
    f2.penup()
    f2.goto(xf2,yf2)
    f2.ondrag(draggingf2)
    
def draggingg2(xg2,yg2):
    g2.ondrag(None)
    g2.penup()
    g2.goto(xg2,yg2)
    g2.ondrag(draggingg2)
    
def draggingh2(xh2,yh2):
    h2.ondrag(None)
    h2.penup()
    h2.goto(xh2,yh2)
    h2.ondrag(draggingh2)
    
def draggingwK(xwK,ywK):
    wK.ondrag(None)
    wK.penup()
    wK.goto(xwK,ywK)
    wK.ondrag(draggingwK)
     
def draggingwQ(xwQ,ywQ):
    wQ.ondrag(None)
    wQ.penup()
    wQ.goto(xwQ,ywQ)
    wQ.ondrag(draggingwQ)
    
def draggingwRa(xwRa,ywRa):
    wRa.ondrag(None)
    wRa.penup()
    wRa.goto(xwRa,ywRa)
    wRa.ondrag(draggingwRa)
    
def draggingwRh(xwRh,ywRh):
    wRh.ondrag(None)
    wRh.penup()
    wRh.goto(xwRh,ywRh)
    wRh.ondrag(draggingwRh)
    
def draggingwNb(xwNb,ywNb):
    wNb.ondrag(None)
    wNb.penup()
    wNb.goto(xwNb,ywNb)
    wNb.ondrag(draggingwNb)
    
def draggingwNg(xwNg,ywNg):
    wNg.ondrag(None)
    wNg.penup()
    wNg.goto(xwNg,ywNg)
    wNg.ondrag(draggingwNg)

def draggingwBc(xwBc,ywBc):
    wBc.ondrag(None)
    wBc.penup()
    wBc.goto(xwBc,ywBc)
    wBc.ondrag(draggingwBc)
    
def draggingwBf(xwBf,ywBf):
    wBf.ondrag(None)
    wBf.penup()
    wBf.goto(xwBf,ywBf)
    wBf.ondrag(draggingwBf)

def dragginga7(xa7,ya7):
    a7.ondrag(None)
    a7.penup()
    a7.goto(xa7,ya7)
    a7.ondrag(dragginga7)




def snapa2(pxa2,pya2):

    if not r:
    
        if -300>pxa2>-400 and -300>pya2>-400:
            a2.goto(-350,-350)
        elif -300>pxa2>-400 and -200>pya2>-300:
            a2.goto(-350,-250)
        elif -300>pxa2>-400 and -100>pya2>-200:
            a2.goto(-350,-150)
        elif -300>pxa2>-400 and 0>pya2>-100:
            a2.goto(-350,-50)
        elif -300>pxa2>-400 and 100>pya2>0:
            a2.goto(-350,50)
        elif -300>pxa2>-400 and 200>pya2>100:
            a2.goto(-350,150)
        elif -300>pxa2>-400 and 300>pya2>200:
            a2.goto(-350,250)
        elif -300>pxa2>-400 and 400>pya2>300:
            a2.goto(-350,350)
        
        elif -200>pxa2>-300 and -300>pya2>-400:
            a2.goto(-250,-350)
        elif -200>pxa2>-300 and -200>pya2>-300:
            a2.goto(-250,-250)
        elif -200>pxa2>-300 and -100>pya2>-200:
            a2.goto(-250,-150)
        elif -200>pxa2>-300 and 0>pya2>-100:
            a2.goto(-250,-50)
        elif -200>pxa2>-300 and 100>pya2>0:
            a2.goto(-250,50)
        elif -200>pxa2>-300 and 200>pya2>100:
            a2.goto(-250,150)
        elif -200>pxa2>-300 and 300>pya2>200:
            a2.goto(-250,250)
        elif -200>pxa2>-300 and 400>pya2>300:
            a2.goto(-250,350)
            
        elif -100>pxa2>-200 and -300>pya2>-400:
            a2.goto(-150,-350)
        elif -100>pxa2>-200 and -200>pya2>-300:
            a2.goto(-150,-250)
        elif -100>pxa2>-200 and -100>pya2>-200:
            a2.goto(-150,-150)
        elif -100>pxa2>-200 and 0>pya2>-100:
            a2.goto(-150,-50)
        elif -100>pxa2>-200 and 100>pya2>0:
            a2.goto(-150,50)
        elif -100>pxa2>-200 and 200>pya2>100:
            a2.goto(-150,150)
        elif -100>pxa2>-200 and 300>pya2>200:
            a2.goto(-150,250)
        elif -100>pxa2>-200 and 400>pya2>300:
            a2.goto(-150,350)
        
        elif 0>pxa2>-100 and -300>pya2>-400:
            a2.goto(-50,-350)
        elif 0>pxa2>-100 and -200>pya2>-300:
            a2.goto(-50,-250)
        elif 0>pxa2>-100 and -100>pya2>-200:
            a2.goto(-50,-150)
        elif 0>pxa2>-100 and 0>pya2>-100:
            a2.goto(-50,-50)
        elif 0>pxa2>-100 and 100>pya2>0:
            a2.goto(-50,50)
        elif 0>pxa2>-100 and 200>pya2>100:
            a2.goto(-50,150)
        elif 0>pxa2>-100 and 300>pya2>200:
            a2.goto(-50,250)
        elif 0>pxa2>-100 and 400>pya2>300:
            a2.goto(-50,350)
        
        elif 100>pxa2>0 and -300>pya2>-400:
            a2.goto(50,-350)
        elif 100>pxa2>0 and -200>pya2>-300:
            a2.goto(50,-250)
        elif 100>pxa2>0 and -100>pya2>-200:
            a2.goto(50,-150)
        elif 100>pxa2>0 and 0>pya2>-100:
            a2.goto(50,-50)
        elif 100>pxa2>0 and 100>pya2>0:
            a2.goto(50,50)
        elif 100>pxa2>0 and 200>pya2>100:
            a2.goto(50,150)
        elif 100>pxa2>0 and 300>pya2>200:
            a2.goto(50,250)
        elif 100>pxa2>0 and 400>pya2>300:
            a2.goto(50,350)
            
        elif 200>pxa2>100 and -300>pya2>-400:
            a2.goto(150,-350)
        elif 200>pxa2>100 and -200>pya2>-300:
            a2.goto(150,-250)
        elif 200>pxa2>100 and -100>pya2>-200:
            a2.goto(150,-150)
        elif 200>pxa2>100 and 0>pya2>-100:
            a2.goto(150,-50)
        elif 200>pxa2>100 and 100>pya2>0:
            a2.goto(150,50)
        elif 200>pxa2>100 and 200>pya2>100:
            a2.goto(150,150)
        elif 200>pxa2>100 and 300>pya2>200:
            a2.goto(150,250)
        elif 200>pxa2>100 and 400>pya2>300:
            a2.goto(150,350)
        
        elif 300>pxa2>200 and -300>pya2>-400:
            a2.goto(250,-350)
        elif 300>pxa2>200 and -200>pya2>-300:
            a2.goto(250,-250)
        elif 300>pxa2>200 and -100>pya2>-200:
            a2.goto(250,-150)
        elif 300>pxa2>200 and 0>pya2>-100:
            a2.goto(250,-50)
        elif 300>pxa2>200 and 100>pya2>0:
            a2.goto(250,50)
        elif 300>pxa2>200 and 200>pya2>100:
            a2.goto(250,150)
        elif 300>pxa2>200 and 300>pya2>200:
            a2.goto(250,250)
        elif 300>pxa2>200 and 400>pya2>300:
            a2.goto(250,350)
        
        elif 400>pxa2>300 and -300>pya2>-400:
            a2.goto(350,-350)
        elif 400>pxa2>300 and -200>pya2>-300:
            a2.goto(350,-250)
        elif 400>pxa2>300 and -100>pya2>-200:
            a2.goto(350,-150)
        elif 400>pxa2>300 and 0>pya2>-100:
            a2.goto(350,-50)
        elif 400>pxa2>300 and 100>pya2>0:
            a2.goto(350,50)
        elif 400>pxa2>300 and 200>pya2>100:
            a2.goto(350,150)
        elif 400>pxa2>300 and 300>pya2>200:
            a2.goto(350,250)
        elif 400>pxa2>300 and 400>pya2>300:
            a2.goto(350,350)


def snapb2(pxb2,pyb2):
    
    if -300>pxb2>-400 and -300>pyb2>-400:
        b2.goto(-350,-350)
    elif -300>pxb2>-400 and -200>pyb2>-300:
        b2.goto(-350,-250)
    elif -300>pxb2>-400 and -100>pyb2>-200:
        b2.goto(-350,-150)
    elif -300>pxb2>-400 and 0>pyb2>-100:
        b2.goto(-350,-50)
    elif -300>pxb2>-400 and 100>pyb2>0:
        b2.goto(-350,50)
    elif -300>pxb2>-400 and 200>pyb2>100:
        b2.goto(-350,150)
    elif -300>pxb2>-400 and 300>pyb2>200:
        b2.goto(-350,250)
    elif -300>pxb2>-400 and 400>pyb2>300:
        b2.goto(-350,350)
    
    elif -200>pxb2>-300 and -300>pyb2>-400:
        b2.goto(-250,-350)
    elif -200>pxb2>-300 and -200>pyb2>-300:
        b2.goto(-250,-250)
    elif -200>pxb2>-300 and -100>pyb2>-200:
        b2.goto(-250,-150)
    elif -200>pxb2>-300 and 0>pyb2>-100:
        b2.goto(-250,-50)
    elif -200>pxb2>-300 and 100>pyb2>0:
        b2.goto(-250,50)
    elif -200>pxb2>-300 and 200>pyb2>100:
        b2.goto(-250,150)
    elif -200>pxb2>-300 and 300>pyb2>200:
        b2.goto(-250,250)
    elif -200>pxb2>-300 and 400>pyb2>300:
        b2.goto(-250,350)
        
    elif -100>pxb2>-200 and -300>pyb2>-400:
        b2.goto(-150,-350)
    elif -100>pxb2>-200 and -200>pyb2>-300:
        b2.goto(-150,-250)
    elif -100>pxb2>-200 and -100>pyb2>-200:
        b2.goto(-150,-150)
    elif -100>pxb2>-200 and 0>pyb2>-100:
        b2.goto(-150,-50)
    elif -100>pxb2>-200 and 100>pyb2>0:
        b2.goto(-150,50)
    elif -100>pxb2>-200 and 200>pyb2>100:
        b2.goto(-150,150)
    elif -100>pxb2>-200 and 300>pyb2>200:
        b2.goto(-150,250)
    elif -100>pxb2>-200 and 400>pyb2>300:
        b2.goto(-150,350)
    
    elif 0>pxb2>-100 and -300>pyb2>-400:
        b2.goto(-50,-350)
    elif 0>pxb2>-100 and -200>pyb2>-300:
        b2.goto(-50,-250)
    elif 0>pxb2>-100 and -100>pyb2>-200:
        b2.goto(-50,-150)
    elif 0>pxb2>-100 and 0>pyb2>-100:
        b2.goto(-50,-50)
    elif 0>pxb2>-100 and 100>pyb2>0:
        b2.goto(-50,50)
    elif 0>pxb2>-100 and 200>pyb2>100:
        b2.goto(-50,150)
    elif 0>pxb2>-100 and 300>pyb2>200:
        b2.goto(-50,250)
    elif 0>pxb2>-100 and 400>pyb2>300:
        b2.goto(-50,350)
    
    elif 100>pxb2>0 and -300>pyb2>-400:
        b2.goto(50,-350)
    elif 100>pxb2>0 and -200>pyb2>-300:
        b2.goto(50,-250)
    elif 100>pxb2>0 and -100>pyb2>-200:
        b2.goto(50,-150)
    elif 100>pxb2>0 and 0>pyb2>-100:
        b2.goto(50,-50)
    elif 100>pxb2>0 and 100>pyb2>0:
        b2.goto(50,50)
    elif 100>pxb2>0 and 200>pyb2>100:
        b2.goto(50,150)
    elif 100>pxb2>0 and 300>pyb2>200:
        b2.goto(50,250)
    elif 100>pxb2>0 and 400>pyb2>300:
        b2.goto(50,350)
        
    elif 200>pxb2>100 and -300>pyb2>-400:
        b2.goto(150,-350)
    elif 200>pxb2>100 and -200>pyb2>-300:
        b2.goto(150,-250)
    elif 200>pxb2>100 and -100>pyb2>-200:
        b2.goto(150,-150)
    elif 200>pxb2>100 and 0>pyb2>-100:
        b2.goto(150,-50)
    elif 200>pxb2>100 and 100>pyb2>0:
        b2.goto(150,50)
    elif 200>pxb2>100 and 200>pyb2>100:
        b2.goto(150,150)
    elif 200>pxb2>100 and 300>pyb2>200:
        b2.goto(150,250)
    elif 200>pxb2>100 and 400>pyb2>300:
        b2.goto(150,350)
    
    elif 300>pxb2>200 and -300>pyb2>-400:
        b2.goto(250,-350)
    elif 300>pxb2>200 and -200>pyb2>-300:
        b2.goto(250,-250)
    elif 300>pxb2>200 and -100>pyb2>-200:
        b2.goto(250,-150)
    elif 300>pxb2>200 and 0>pyb2>-100:
        b2.goto(250,-50)
    elif 300>pxb2>200 and 100>pyb2>0:
        b2.goto(250,50)
    elif 300>pxb2>200 and 200>pyb2>100:
        b2.goto(250,150)
    elif 300>pxb2>200 and 300>pyb2>200:
        b2.goto(250,250)
    elif 300>pxb2>200 and 400>pyb2>300:
        b2.goto(250,350)
    
    elif 400>pxb2>300 and -300>pyb2>-400:
        b2.goto(350,-350)
    elif 400>pxb2>300 and -200>pyb2>-300:
        b2.goto(350,-250)
    elif 400>pxb2>300 and -100>pyb2>-200:
        b2.goto(350,-150)
    elif 400>pxb2>300 and 0>pyb2>-100:
        b2.goto(350,-50)
    elif 400>pxb2>300 and 100>pyb2>0:
        b2.goto(350,50)
    elif 400>pxb2>300 and 200>pyb2>100:
        b2.goto(350,150)
    elif 400>pxb2>300 and 300>pyb2>200:
        b2.goto(350,250)
    elif 400>pxb2>300 and 400>pyb2>300:
        b2.goto(350,350)


#turtle.onclick(a2.ondrag(dragginga2))
turtle.onclick(b2.ondrag(draggingb2))
turtle.onclick(c2.ondrag(draggingc2))
turtle.onclick(d2.ondrag(draggingd2))
turtle.onclick(e2.ondrag(dragginge2))
turtle.onclick(f2.ondrag(draggingf2))
turtle.onclick(g2.ondrag(draggingg2))
turtle.onclick(h2.ondrag(draggingh2))

turtle.onclick(wRa.ondrag(draggingwRa))
turtle.onclick(wRh.ondrag(draggingwRh))
turtle.onclick(wNb.ondrag(draggingwNb))
turtle.onclick(wNg.ondrag(draggingwNg))
turtle.onclick(wBc.ondrag(draggingwBc))
turtle.onclick(wBf.ondrag(draggingwBf))
turtle.onclick(wK.ondrag(draggingwK))
turtle.onclick(wQ.ondrag(draggingwQ))

turtle.onclick(a7.ondrag(dragginga7))

a2.ondrag(dragginga2)

x1=-300
x2=-400
y1=-200
y2=-300
px=(x1+x2)/2
py=(y1+y2)/2
range1=8
range2=range1+6
range3=range1+7

turtle.listen()
turtle.tracer(n=10,delay=0)

def rf():
    global r
    r = False

while True:
    pxa2=a2.xcor()
    pya2=a2.ycor()
    
    pxb2=b2.xcor()
    pyb2=b2.ycor()

    turtle.onrelease(rf)

    turtle.onkeyrelease(snapb2(pxb2,pyb2), 1)

    a2.onrelease(snapa2(pxa2,pya2),True)
    #b2.onrelease(snapb2(pxb2,pyb2),True)
    
    #turtle.listen()
    #turtle.onrelease(snapa2(pxa2,pya2))
    #turtle.onrelease(snapb2(pxb2,pyb2))
    '''
    if -300>a2.xcor()>-400 and -300>a2.ycor()>-400:
        a2.goto(-350,-350)


    for w in range(63):
        elif x1>a2.xcor()>x2 and y1>a2.ycor()>y2:
                a2.goto(px,py)
        
        if 0<=i<=6:
            y1+=100
            y2+=100
        elif i==7:
            x1+=100
            x2+=100
        
        for ww in range(8):
            elif range1<=i<=range2:
                y1+=100
                y2+=100
            elif i==range3:
                x1+=100
                x2+=100
            range1+=8
    '''     
    
    s.update()

