'''
import turtle

func=input("Enter a polynomial function: ")

var_holder = {}

neg1=func.find("-")
if neg1==0:
    coef1neg=func.partition("-")
    posfunc=coef1neg[2]
    numb1=posfunc.count("+")
    numb2=posfunc.count("-")
    terms=numb1+numb2+1
else:
    numb1=func.count("+")
    numb2=func.count("-")
    terms=numb1+numb2+1
    
dfunc=func
    
for i in range(terms):
    neg1=func.find("-")
    if neg1==0:
        coef1neg=func.partition("-")
        posfunc=coef1neg[2]
        negapos1=posfunc.find("+")
        neganeg1=posfunc.find("-")
        if neganeg1==-1:
            if negapos1==-1:
                xdegree1st="-"+posfunc
            else:
                part1=posfunc.partition("+")
                xdegree1st="-"+part1[0]
        elif negapos1==-1:
            part1=posfunc.partition("-")
            xdegree1st="-"+part1[0]
        elif negapos1<neganeg1:
            part1=posfunc.partition("+")
            xdegree1st="-"+part1[0]
        else:
            part1=posfunc.partition("-")
            xdegree1st="-"+part1[0]
    elif neg1==-1:
        pos1=func.find("+")
        if pos1==-1:
            xdegree1st=func
        else:
            part1=func.partition("+")
            xdegree1st=part1[0]
    else:
        pos1=func.find("+")
        if pos1==-1:
            part1=func.partition("-")
            xdegree1st=part1[0]
        elif pos1<neg1:
            part1=func.partition("+")
            xdegree1st=part1[0]
        else:
            part1=func.partition("-")
            xdegree1st=part1[0]
    var_holder['term_no_' + str(i)] = xdegree1st
    if terms>2:
        func=part1[2]
    else:
        break
locals().update(var_holder)

oper="0"
'''
'''
for j in range(terms):
    neg=dfunc.find("-")
    pos=dfunc.find("+")
    if neg==0:
'''
'''
print(term_no_2) 
'''  
'''
       
from turtle import *

s = Screen()
s.delay(0)
setworldcoordinates(0, 0, 200, 200)

b1 = Turtle()
b2 = Turtle()
t = Turtle()

#t.ht()

b1.pu()
b2.pu()
t.pu()

b1.speed(0)
b2.speed(0)
t.speed(0)

b1.goto(100,100)
b2.goto(-100,100)

def drag(x,y):
    global b1x, b1y, b2x, b2y
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(drag)

    b1x = t.xcor() + db1x
    b1y = t.ycor() + db1y

    b2x = t.xcor() + db2x
    b2y = t.ycor() + db2y

    b1.goto(b1x,b1y)
    b2.goto(b2x,b2y)

def dragged(x,y):
    global db1x, db1y, db2x, db2y
    t.goto(x,y)
    t.ondrag(drag)

    
    if t.xcor() < b1.xcor():
        if t.ycor() < b1.ycor():
            db1x = abs(abs(t.xcor()) - abs(b1.xcor()))
            db1y = abs(abs(t.ycor()) - abs(b1.ycor()))
        elif t.ycor() > b1.ycor():
            db1x = abs(abs(t.xcor()) - abs(b1.xcor()))
            db1y = -(abs(abs(t.ycor()) - abs(b1.ycor())))
        else:
            db1x = abs(abs(t.xcor()) - abs(b1.xcor()))
            db1y = 0
    elif t.xcor() > b1.xcor():
        if t.ycor() < b1.ycor():
            db1x = -(abs(abs(t.xcor()) - abs(b1.xcor())))
            db1y = abs(abs(t.ycor()) - abs(b1.ycor()))
        elif t.ycor() > b1.ycor():
            db1x = -(abs(abs(t.xcor()) - abs(b1.xcor())))
            db1y = -(abs(abs(t.ycor()) - abs(b1.ycor())))
        else:
            db1x = -(abs(abs(t.xcor()) - abs(b1.xcor())))
            db1y = 0
    else:
        if t.ycor() < b1.ycor():
            db1x = 0
            db1y = abs(abs(t.ycor()) - abs(b1.ycor()))
        elif t.ycor() > b1.ycor():
            db1x = 0
            db1y = -(abs(abs(t.ycor()) - abs(b1.ycor())))
        else:
            db1x = 0
            db1y = 0

    if t.xcor() < b2.xcor():
        if t.ycor() < b2.ycor():
            db2x = abs(abs(t.xcor()) - abs(b2.xcor()))
            db2y = abs(abs(t.ycor()) - abs(b2.ycor()))
        elif t.ycor() > b2.ycor():
            db2x = abs(abs(t.xcor()) - abs(b2.xcor()))
            db2y = -(abs(abs(t.ycor()) - abs(b2.ycor())))
        else:
            db2x = abs(abs(t.xcor()) - abs(b2.xcor()))
            db2y = 0
    elif t.xcor() > b2.xcor():
        if t.ycor() < b2.ycor():
            db2x = -(abs(abs(t.xcor()) - abs(b2.xcor())))
            db2y = abs(abs(t.ycor()) - abs(b2.ycor()))
        elif t.ycor() > b2.ycor():
            db2x = -(abs(abs(t.xcor()) - abs(b2.xcor())))
            db2y = -(abs(abs(t.ycor()) - abs(b2.ycor())))
        else:
            db2x = -(abs(abs(t.xcor()) - abs(b2.xcor())))
            db2y = 0
    else:
        if t.ycor() < b2.ycor():
            db2x = 0
            db2y = abs(abs(t.ycor()) - abs(b2.ycor()))
        elif t.ycor() > b2.ycor():
            db2x = 0
            db2y = -(abs(abs(t.ycor()) - abs(b2.ycor())))
        else:
            db2x = 0
            db2y = 0
        

s.onscreenclick(dragged)

s.mainloop()
'''
from tkinter import *
from tkinter import font

root = Tk()
root.title('Font Families')
fonts=list(font.families())
fonts.sort()

def populate(frame):
    '''Put in the fonts'''
    listnumber = 1
    for item in fonts:
        label = "listlabel" + str(listnumber)
        label = Label(frame,text=item,font=(item, 16)).pack()
        listnumber += 1

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()
