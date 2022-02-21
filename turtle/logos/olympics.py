import turtle
import math
s=turtle.getscreen()
turtle.title("Olympics")
t=turtle.Turtle()
turtle.ht()
t.speed(6)
t.pensize(11.7)
t.pencolor("black")

t.penup()
t.goto(0,-100)
t.pendown()

t.circle(100)

t.penup()
t.goto(-220,-100)
t.pendown()

t.pencolor("#247291")
t.circle(100)

t.penup()
t.goto(220,-100)
t.pendown()

t.pencolor("#ED334F")
t.circle(100)

t.penup()
t.goto(-110,-200)
t.pendown()

t.pencolor("#FBB132")
t.circle(100)

t.penup()
t.goto(110,-200)
t.pendown()

t.pencolor("#1C8B3B")
t.circle(100)

#overlaps:

t.penup()
t.goto(220,-100)
t.lt(180)
t.pendown()

t.pencolor("#ED334F")
t.circle(-100,45)

t.penup()
t.home()
t.lt(180)
t.goto(0,-100)
t.pendown()

t.pencolor("black")
t.circle(-100,45)

t.penup()
t.lt(180)
t.goto(50*math.sqrt(2)-0.5,50*math.sqrt(2)-0.5)
t.pendown()

t.circle(-100,90)

t.penup()
t.home()
t.goto(-220,0)
t.fd(50*math.sqrt(2)-0.5)
t.lt(90)
t.fd(50*math.sqrt(2)-0.5)
t.rt(135)
t.pendown()

t.pencolor("#247291")
t.circle(-100,90)