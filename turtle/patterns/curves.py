import turtle

x = int(input("Enter the scale: "))

s=turtle.getscreen()
turtle.title("Shuriken")
turtle.ht()
#s.bgcolor("black")
s.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.fillcolor("#891300")
t.ht()

def clear():
    t.clear()

def fcircle():
    t.circle(x)
    
def forward():
    t.fd(x)
    
def backward():
    t.bk(x)
    
def left():
    t.lt(90)
    
def right():
    t.rt(90)
    
turtle.listen()
turtle.onkeypress(fcircle,"5")
turtle.onkeypress(forward,"w")
turtle.onkeypress(backward,"s")
turtle.onkeypress(left,"a")
turtle.onkeypress(right,"d")
turtle.onkeypress(clear,"-")

turtle.mainloop()
