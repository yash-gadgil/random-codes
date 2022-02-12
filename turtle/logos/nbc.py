import turtle
s=turtle.getscreen()
turtle.title("NBC Logo")
t=turtle.Turtle()
turtle.ht()
t.speed(0)
t.pensize(2)
t.pencolor("#0DB14B")
f=18.75

def pfeather(color):
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)
    t.fd(173.9)
    t.circle(50,211.5)
    t.fd(173.9)
    t.end_fill()

def nfeather(color):
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)
    t.fd(173.9)
    t.circle(-50,211.5)
    t.fd(173.9)
    t.end_fill()

#lift
t.penup()
t.fd(f)
t.pendown()

#green
pfeather("#0DB14B")

#lift
t.penup()
t.home()
t.lt(180)
t.fd(f)
t.pendown()

#yellow
nfeather("#FCB711")

#lift
t.penup()
t.home()
t.goto(f,0)
t.fd(10.5)
t.lt(90)
t.fd(23.5)
t.rt(26.5)
t.pendown()

#blue
nfeather("#0089D0")

#lift
t.penup()
t.home()
t.lt(180)
t.fd(f)
t.fd(10.5)
t.rt(90)
t.fd(21.3)
t.lt(57.9)
t.pendown()

#orange
nfeather("#F37021")

#lift
t.penup()
t.home()
t.goto(f,0)
t.fd(10.5)
t.lt(90)
t.fd(23.5)
t.rt(26.5)
t.fd(10.5)
t.lt(90)
t.fd(12.5)
t.rt(57.9)
t.pendown()

#purple
nfeather("#6460AA")

#lift
t.penup()
t.home()
t.lt(180)
t.goto(-f,0)
t.fd(10.5)
t.rt(90)
t.fd(23.5)
t.lt(26.5)
t.fd(10.5)
t.rt(90)
t.fd(11.5)
t.lt(88.9)
t.pendown()

#dark red
nfeather("#CC004C")

#lift
t.penup()
t.home()
t.goto(f,0)
t.fd(10.5)
t.lt(90)
t.fd(23.5)
t.rt(26.5)
t.fd(10.5)
t.lt(90)
t.fd(12.5)
t.rt(57.9)
t.fd(159.9)
t.pendown()

#beak
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(-10,70)
t.fd(10)
t.lt(100)
t.circle(5,50)
t.fd(18)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(7)
t.end_fill()

#lift
t.penup()
h=217.65
t.home()
t.goto(-h,-30)
t.pendown()

#N
t.pencolor("black")
t.fillcolor("black")
t.begin_fill()
t.rt(44)
t.fd(154)
t.lt(134)
t.fd(102.3)
t.rt(90)
t.fd(37.4)
t.rt(90)
t.fd(184.8)
t.rt(134)
t.fd(154)
t.lt(134)
t.fd(102.3)
t.rt(90)
t.fd(37.4)
t.rt(90)
t.fd(184.8)
t.end_fill()

#lift
t.penup()
t.home()
t.goto(-51.65,-34.677389051)
t.pendown()

#B
t.begin_fill()
t.fd(79.2)
t.circle(-41.8,178)
t.lt(178)
t.lt(90)
t.fd(4)
t.rt(90)
t.circle(-47.8,180)
t.fd(80.2)
t.end_fill()
t.fillcolor("white")
t.penup()
t.home()
t.goto(-19.37,-61.45072238)
t.pendown()
t.begin_fill()
t.fd(30.8)
t.circle(-21.23,180)
t.fd(30.8)
t.end_fill()
t.penup()
t.rt(180)
t.goto(-19.37,-137.22405571)
t.begin_fill()
t.fd(35.2)
t.circle(-23.21,180)
t.fd(35.2)
t.end_fill()

t.pensize(4)
t.penup()
t.goto(42.5,-121.1)
t.pendown()
t.rt(40)
t.fd(7)
t.lt(130)
t.fd(2)
t.lt(100)
t.fd(7)
t.ht()

#lift
l=172.65
t.penup()
t.home()
t.goto(l,-34.677389051)
t.pendown()

#C
t.fillcolor("black")
t.begin_fill()
t.circle(-91.1)
t.end_fill()
t.goto(l,-65.917389051)
t.fillcolor("white")
t.begin_fill()
t.circle(-59.86)
t.end_fill()
t.penup()
t.goto(207.65,-34.677389051)
t.pendown()
t.pencolor("white")
t.begin_fill()
t.rt(90)
t.fd(200)
t.lt(90)
t.fd(90)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(90)
t.end_fill()

t.ht()
