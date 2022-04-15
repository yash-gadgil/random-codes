
import turtle
import math
import tkinter

s = turtle.getscreen()
s.delay(0)
turtle.title("Input")
turtle.ht()

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

t1 = turtle.Turtle()
t1.speed(0)
t1.pensize(3)
t1.penup()
t1.ht()

xnot = turtle.Turtle()
xnot.speed(0)
xnot.pensize(8)
xnot.penup()
xnot.ht()

input0 = ""
inloop = ""
loop = False
xno = False
playerxwin = False
playerowin = False
scale = 100

def dragxno(x,y):
    if xno:
        global player1
        global player2
        
        global topmidx
        global topleftx
        global toprightx
        global midmidx
        global midleftx
        global midrightx
        global botmidx
        global botleftx
        global botrightx
        global topmido
        global toplefto
        global toprighto
        global midmido
        global midlefto
        global midrighto
        global botmido
        global botlefto
        global botrighto
        
        global playerxwin
        global playerowin

        xnot.goto(x,y)
        
        if player1:
            xnot.fillcolor("#cc1d00")
            if -100<xnot.xcor()<100 and -100<xnot.ycor()<100:
                if not midmidx:
                    if not midmido:
                        
                        xnot.goto(-100,-100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-80,-80)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        midmidx = True
                        
                        xnot.home()
                
            elif -300<xnot.xcor()<-100 and -100<xnot.ycor()<100:
                if not midleftx:
                    if not midlefto:
                        
                        xnot.goto(-300,-100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-280,-80)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        midleftx = True
                        
                        xnot.home()
                
            elif 100<xnot.xcor()<300 and -100<xnot.ycor()<100:
                if not midrightx:
                    if not midrighto:
                        
                        xnot.goto(100,-100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(120,-80)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        midrightx = True
                        
                        xnot.home()
            
            elif -100<xnot.xcor()<100 and 100<xnot.ycor()<300:
                if not topmidx:
                    if not topmido:
                        
                        xnot.goto(-100,100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-80,120)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        topmidx = True
                        
                        xnot.home()
                
            elif -300<xnot.xcor()<-100 and 100<xnot.ycor()<300:
                if not topleftx:
                    if not toplefto:
                        
                        xnot.goto(-300,100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-280,120)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        topleftx = True
                        
                        xnot.home()
                
            elif 100<xnot.xcor()<300 and 100<xnot.ycor()<300:
                if not toprightx:
                    if not toprighto:
                        
                        xnot.goto(100,100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(120,120)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        toprightx = True
                        
                        xnot.home()
                
            elif -100<xnot.xcor()<100 and -300<xnot.ycor()<-100:
                if not botmidx:
                    if not botmido:
                        
                        xnot.goto(-100,-300)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-80,-280)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        botmidx = True
                        
                        xnot.home()
                
            elif -300<xnot.xcor()<-100 and -300<xnot.ycor()<-100:
                if not botleftx:
                    if not botlefto:
                        
                        xnot.goto(-300,-300)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-280,-280)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        botleftx = True
                        
                        xnot.home()
                
            elif 100<xnot.xcor()<300 and -300<xnot.ycor()<-100:
                if not botrightx:
                    if not botrighto:
                        
                        xnot.goto(100,-300)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(120,-280)
                        
                        xnot.pendown()
                        
                        xnot.lt(45)
                        xnot.fd(160*math.sqrt(2))
                        xnot.bk(80*math.sqrt(2))
                        xnot.lt(90)
                        xnot.fd(80*math.sqrt(2))
                        xnot.bk(160*math.sqrt(2))
                        
                        xnot.penup()
                        
                        player1 = False
                        player2 = True
                        botrightx = True
                        
                        xnot.home()
                        
        elif player2:
            xnot.fillcolor("#17517e")
            
            if -100<xnot.xcor()<100 and -100<xnot.ycor()<100:
                if not midmido:
                    if not midmidx:
                        
                        xnot.goto(-100,-100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(0,-80)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        midmido = True
                        
                        xnot.home()
                
            elif -300<xnot.xcor()<-100 and -100<xnot.ycor()<100:
                if not midlefto:
                    if not midleftx:
                        
                        xnot.goto(-300,-100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-200,-80)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        midlefto = True
                        
                        xnot.home()
                
            elif 100<xnot.xcor()<300 and -100<xnot.ycor()<100:
                if not midrighto:
                    if not midrightx:
                        
                        xnot.goto(100,-100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(200,-80)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        midrighto = True
                        
                        xnot.home()
            
            elif -100<xnot.xcor()<100 and 100<xnot.ycor()<300:
                if not topmido:
                    if not topmidx:
                        
                        xnot.goto(-100,100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(0,120)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        topmido = True
                        
                        xnot.home()
                
            elif -300<xnot.xcor()<-100 and 100<xnot.ycor()<300:
                if not toplefto:
                    if not topleftx:
                        
                        xnot.goto(-300,100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-200,120)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        toplefto = True
                        
                        xnot.home()
                
            elif 100<xnot.xcor()<300 and 100<xnot.ycor()<300:
                if not toprighto:
                    if not toprightx:
                        
                        xnot.goto(100,100)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(200,120)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        toprighto = True
                        
                        xnot.home()
                
            elif -100<xnot.xcor()<100 and -300<xnot.ycor()<-100:
                if not botmido:
                    if not botmidx:
                        
                        xnot.goto(-100,-300)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(0,-280)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        botmido = True
                        
                        xnot.home()
                
            elif -300<xnot.xcor()<-100 and -300<xnot.ycor()<-100:
                if not botlefto:
                    if not botleftx:
                        
                        xnot.goto(-300,-300)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(-200,-280)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        botlefto = True
                        
                        xnot.home()
                
            elif 100<xnot.xcor()<300 and -300<xnot.ycor()<-100:
                if not botrighto:
                    if not botrightx:
                        
                        xnot.goto(100,-300)
                        
                        xnot.pensize(3)
                        xnot.pendown()
                        xnot.begin_fill()
                        
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        xnot.fd(200)
                        xnot.lt(90)
                        
                        xnot.end_fill()
                        xnot.penup()
                        xnot.pensize(8)
                        
                        xnot.goto(200,-280)
                        
                        xnot.pendown()
                        
                        xnot.circle(80)
                        
                        xnot.penup()
                        
                        player1 = True
                        player2 = False
                        botrighto = True
                        
                        xnot.home()
        if (topleftx and topmidx and toprightx) or (midleftx and midmidx and midrightx) or (botleftx and botmidx and botrightx) or (topleftx and midleftx and botleftx) or (topmidx and midmidx and botmidx) or (toprightx and midrightx and botrightx) or (topleftx and midmidx and botrightx) or (toprightx and midmidx and botleftx):
            
            t1.penup()
            t1.goto(-160,400)
            t1.pendown()
            
            t1.write("Player 1 Wins!", font=("Arial",36,"bold"))
            
            t1.penup()
            t1.goto(-80,370)
            t1.pendown()
            
            t1.write("type exit to exit", font=("Arial",18,"bold"))
            
            t1.penup()
            
            playerxwin = True
            
        elif (toplefto and topmido and toprighto) or (midlefto and midmido and midrighto) or (botlefto and botmido and botrighto) or (toplefto and midlefto and botlefto) or (topmido and midmido and botmido) or (toprighto and midrighto and botrighto) or (toplefto and midmido and botrighto) or (toprighto and midmido and botlefto):
            
            t1.penup()
            t1.goto(-160,400)
            t1.pendown()
            
            t1.write("Player 2 Wins!", font=("Arial",36,"bold"))
            
            t1.penup()
            t1.goto(-80,370)
            t1.pendown()
            
            t1.write("type exit to exit", font=("Arial",18,"bold"))
            
            t1.penup()
            
            playerowin = True

def one():
    global input0
    input0 = input0 + "1"

def two():
    global input0
    input0 = input0 + "2"
    
def three():
    global input0
    input0 = input0 + "3"
    
def four():
    global input0
    input0 = input0 + "4"
    
def five():
    global input0
    input0 = input0 + "5"
    
def six():
    global input0
    input0 = input0 + "6"
    
def seven():
    global input0
    input0 = input0 + "7"
    
def eight():
    global input0
    input0 = input0 + "8"
    
def nine():
    global input0
    input0 = input0 + "9"
    
def zero():
    global input0
    input0 = input0 + "0"

def a():
    global input0
    input0 = input0 + "a"

def b():
    global input0
    input0 = input0 + "b"

def c():
    global input0
    input0 = input0 + "c"

def d():
    global input0
    input0 = input0 + "d"
    
def e():
    global input0
    input0 = input0 + "e"

def f():
    global input0
    input0 = input0 + "f"

def g():
    global input0
    input0 = input0 + "g"

def h():
    global input0
    input0 = input0 + "h"

def i():
    global input0
    input0 = input0 + "i"

def j():
    global input0
    input0 = input0 + "j"
    
def k():
    global input0
    input0 = input0 + "k"

def l():
    global input0
    input0 = input0 + "l"

def m():
    global input0
    input0 = input0 + "m"

def n():
    global input0
    input0 = input0 + "n"

def o():
    global input0
    input0 = input0 + "o"

def p():
    global input0
    input0 = input0 + "p"
   
def q():
    global input0
    input0 = input0 + "q"

def r():
    global input0
    input0 = input0 + "r"
    
def sw():
    global input0
    input0 = input0 + "s"

def tw():
    global input0
    input0 = input0 + "t"

def u():
    global input0
    input0 = input0 + "u"

def v():
    global input0
    input0 = input0 + "v"
  
def w():
    global input0
    input0 = input0 + "w"

def x():
    global input0
    input0 = input0 + "x"

def y():
    global input0
    input0 = input0 + "y"

def z():
    global input0
    input0 = input0 + "z"


def A():
    global input0
    input0 = input0 + "A"

def B():
    global input0
    input0 = input0 + "B"

def C():
    global input0
    input0 = input0 + "C"

def D():
    global input0
    input0 = input0 + "D"
    
def E():
    global input0
    input0 = input0 + "E"

def F():
    global input0
    input0 = input0 + "F"

def G():
    global input0
    input0 = input0 + "G"

def H():
    global input0
    input0 = input0 + "H"

def I():
    global input0
    input0 = input0 + "I"

def J():
    global input0
    input0 = input0 + "J"
    
def K():
    global input0
    input0 = input0 + "K"

def L():
    global input0
    input0 = input0 + "L"

def M():
    global input0
    input0 = input0 + "M"

def N():
    global input0
    input0 = input0 + "N"

def O():
    global input0
    input0 = input0 + "O"

def P():
    global input0
    input0 = input0 + "P"
   
def Q():
    global input0
    input0 = input0 + "Q"

def R():
    global input0
    input0 = input0 + "R"
    
def Sw():
    global input0
    input0 = input0 + "S"

def Tw():
    global input0
    input0 = input0 + "T"

def U():
    global input0
    input0 = input0 + "U"

def V():
    global input0
    input0 = input0 + "V"
  
def W():
    global input0
    input0 = input0 + "W"

def X():
    global input0
    input0 = input0 + "X"

def Y():
    global input0
    input0 = input0 + "Y"

def Z():
    global input0
    input0 = input0 + "Z"


def clear():
    global input0
    input0 = ""
    
def ast():
    global input0
    input0 = input0 + "*"
    
def space():
    global input0
    input0 = input0 + " "

turtle.listen()

turtle.onkeypress(one,"1")
turtle.onkeypress(two,"2")
turtle.onkeypress(three,"3")
turtle.onkeypress(four,"4")
turtle.onkeypress(five,"5")
turtle.onkeypress(six,"6")
turtle.onkeypress(seven,"7")
turtle.onkeypress(eight,"8")
turtle.onkeypress(nine,"9")
turtle.onkeypress(zero,"0")

turtle.onkeypress(a,"a")
turtle.onkeypress(b,"b")
turtle.onkeypress(c,"c")
turtle.onkeypress(d,"d")
turtle.onkeypress(e,"e")
turtle.onkeypress(f,"f")
turtle.onkeypress(g,"g")
turtle.onkeypress(h,"h")
turtle.onkeypress(i,"i")
turtle.onkeypress(j,"j")
turtle.onkeypress(k,"k")
turtle.onkeypress(l,"l")
turtle.onkeypress(m,"m")
turtle.onkeypress(n,"n")
turtle.onkeypress(o,"o")
turtle.onkeypress(p,"p")
turtle.onkeypress(q,"q")
turtle.onkeypress(r,"r")
turtle.onkeypress(sw,"s")
turtle.onkeypress(tw,"t")
turtle.onkeypress(u,"u")
turtle.onkeypress(v,"v")
turtle.onkeypress(w,"w")
turtle.onkeypress(x,"x")
turtle.onkeypress(y,"y")
turtle.onkeypress(z,"z")

turtle.onkeypress(A,"A")
turtle.onkeypress(B,"B")
turtle.onkeypress(C,"C")
turtle.onkeypress(D,"D")
turtle.onkeypress(E,"E")
turtle.onkeypress(F,"F")
turtle.onkeypress(G,"G")
turtle.onkeypress(H,"H")
turtle.onkeypress(I,"I")
turtle.onkeypress(J,"J")
turtle.onkeypress(K,"K")
turtle.onkeypress(L,"L")
turtle.onkeypress(M,"M")
turtle.onkeypress(N,"N")
turtle.onkeypress(O,"O")
turtle.onkeypress(P,"P")
turtle.onkeypress(Q,"Q")
turtle.onkeypress(R,"R")
turtle.onkeypress(Sw,"S")
turtle.onkeypress(Tw,"T")
turtle.onkeypress(U,"U")
turtle.onkeypress(V,"V")
turtle.onkeypress(W,"W")
turtle.onkeypress(X,"X")
turtle.onkeypress(Y,"Y")
turtle.onkeypress(Z,"Z")

turtle.onkeypress(clear,"/")
turtle.onkeypress(ast,"*")
turtle.onkeypress(space," ")

t.penup()
t.goto(-200,200)
t.pendown()


t.write("type [commands] to see the commands", font=("Arial",18,"bold"))

t.penup()
t.goto(-100,180)
t.pendown()

t.write("type [clear] to clear the screen", font=("Arial",13,"bold"))

t.penup()
t.goto(0,0)
t.pendown()

while True:
    
    if input0 == "clear":
        t.clear()
        input0 = ""
    
    if playerxwin or playerowin:
        if input0 == "exit":
            t.clear()
            t1.clear()
            xnot.clear()
            s.bgcolor("white")
            t.penup()
            t.home()
            t.pendown()
            t1.ht()
            t.st()
            
            xno = False
            playerxwin = False
            playerowin = False
            
            input0 = ""
    
    elif input0 == "home":
        t.penup()
        t.home()
        t.pendown()
        input0 = ""
    
    elif input0 == "circle":
        t.circle(scale)
        
        if loop:
            inloop = inloop + "O"
        
        input0 = ""
        
    elif input0 == "commands":
        
        commandtab = tkinter.Tk()
        
        TextWidget = tkinter.Text(commandtab, height = 40, width = 100)
        
        Label = tkinter.Label(commandtab, text = "Command List")
        Label.config(font =("Courier", 21))
        
        commandlist = '''\tclear - clears screen\n
        home - returns turtle to the center of the screen\n
        circle - creates a circle of the current scale to the left of the turtle\n 
        square - creates a square of the current scale to the left of the turtle\n
        turnright - makes the turtle turn right\n
        turnleft - makes the turtle turn left\n
        forward - turtle covers a distance equal to the current scale in the forward direction\n
        penup - turtle does not draw while the pen is up\n
        pendown - puts the pen down so the turtle can draw\n
        startfill - starts the fill\n
        endfill - ends the fill\n
        turnback - the turtle turns 180 degrees\n
        hide - hides the turtle\n
        show - shows the turtle\n
        xno - starts a game of X and O between 2 players\n
        exit(when in xno) - exits the game of X and O\n
        exit - exits the code\n
        (enter the color name/hex code)*fillcolor - changes the fillcolor to a custom one\n
        (enter a number for the scale)scale - changes the scale\n
        (enter words or numbers)*type - types what the user specified\n'''
        
        exittk = tkinter.Button(commandtab, text = "Continue Input", command = commandtab.quit)
        
        TextWidget.pack()
        Label.pack()
        exittk.pack()
        
        TextWidget.insert(tkinter.END,commandlist)
        
        input0 = ""
        
        tkinter.mainloop()
        
    elif input0 == "square":
        t.rt(45)
        t.circle(scale/math.sqrt(2),360,4)
        t.lt(45)
        
        if loop:
            inloop = inloop + "4"
        
        input0 = ""
        
    elif input0 == "turnright":
        t.rt(90)
        
        if loop:
            inloop = inloop + "R"
        
        input0 = ""
        
    elif input0 == "turnleft":
        t.lt(90)
        
        if loop:
            inloop = inloop + "L"
        
        input0 = ""
        
    elif input0 == "forward":
        t.fd(scale)
        
        if loop:
            inloop = inloop + "F"
        
        input0 = ""
    
    elif input0 == "penup":
        t.penup()
        
        if loop:
            inloop = inloop + "u"
        
        input0 = ""
        
    elif input0 == "pendown":
        t.pendown()
        
        if loop:
            inloop = inloop + "d"
        
        input0 = ""
        
    elif input0 == "startfill":
        t.begin_fill()
        
        if loop:
            inloop = inloop + "S"
        
        input0 = ""
        
    elif input0 == "endfill":
        t.end_fill()
        
        if loop:
            inloop = inloop + "E"
        
        input0 = ""
        
    elif "*fillcolor" in input0:
        fillC = input0.partition("*fillcolor")
        fillc = fillC[0]
        t.fillcolor(fillc)
        input0 = ""
        
    elif input0 == "turnback":
        t.lt(180)
        
        if loop:
            inloop = inloop + "U"
        
        input0 = ""
        
    elif input0 == "hide":
        t.ht()
        input0 = ""
        
    elif input0 == "show":
        t.st()
        input0 = ""
        
    elif "*type" in input0:
        textT = input0.partition("*type")
        text = textT[0]
        t.write(text, font=("Arial",11,"bold"))
        input0 = ""
    
    elif "startloop" in input0:
        loop = True
        input0 = ""
    
    elif "endloop" in input0:
        loop = False
        
        t.clear()
        
        while True:
            for step in inloop:
                if step == "O":
                    t.circle(scale)
                elif step == "4":
                    t.rt(45)
                    t.circle(scale/math.sqrt(2),360,4)
                    t.lt(45)
                elif step == "R":
                    t.rt(90)
                elif step == "L":
                    t.lt(90)
                elif step == "F":
                    t.fd(scale)
                elif step == "u":
                    t.penup()
                elif step == "d":
                    t.pendown()
                elif step == "S":
                    t.begin_fill()
                elif step == "E":
                    t.end_fill()
                elif step == "U":
                    t.rt(180)
        
        input0 = ""
    
    elif "scale" in input0:
        scale = 0
        scale1 = input0.partition("scale")
        scale = int(scale1[0])
        input0 = ""
        
    elif input0 == "xno":
        
        xno = True
        
        player1 = True
        player2 = False
        
        topmidx = False
        topleftx = False
        toprightx = False
        midmidx = False
        midleftx = False
        midrightx = False
        botmidx = False
        botleftx = False
        botrightx = False
        
        topmido = False
        toplefto = False
        toprighto = False
        midmido = False
        midlefto = False
        midrighto = False
        botmido = False
        botlefto = False
        botrighto = False
        
        playerxwin = False
        playerowin = False
        
        s.bgcolor("grey")
        t.clear()
        t.ht()
        
        t1.goto(-300,-300)
        
        t1.pendown()
        
        t1.rt(45)
        t1.circle(300*math.sqrt(2),360,4)
        
        for i in range(3):
            t1.circle(100*math.sqrt(2),360,4)
            t1.sety(t1.ycor()+200)
            t1.circle(100*math.sqrt(2),360,4)
            t1.sety(t1.ycor()+200)
            t1.circle(100*math.sqrt(2),360,4)
            
            if i<3:
                t1.sety(t1.ycor()-400)
                t1.setx(t1.xcor()+200)
        
        t1.penup()
        
        turtle.listen()
        s.onscreenclick(dragxno)
        
        input0 = ""
    
    if input0 == "exit":
        turtle.bye()
    
    s.update()
