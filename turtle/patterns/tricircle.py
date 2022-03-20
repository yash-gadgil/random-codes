import turtle

s=turtle.getscreen()
turtle.title("tri")
turtle.ht()
#s.bgcolor("black")
s.bgcolor("white")
s.delay(0)

t1 = turtle.Turtle()
t1.speed(0)
t1.pensize(3)
t1.fillcolor("#891300") #red

t2 = turtle.Turtle()
t2.speed(0)
t2.lt(120)
t2.pensize(3)
t2.fillcolor("#0D98BA") #green

t3 = turtle.Turtle()
t3.speed(0)
t3.rt(120)
t3.pensize(3)
t3.fillcolor("#FDDA0D") #yellow


t4 = turtle.Turtle()
t4.speed(0)
t4.pensize(3)
t4.fillcolor("#891300") #red

t5 = turtle.Turtle()
t5.speed(0)
t5.lt(120)
t5.pensize(3)
t5.fillcolor("#0D98BA") #green

t6 = turtle.Turtle()
t6.speed(0)
t6.rt(120)
t6.pensize(3)
t6.fillcolor("#FDDA0D") #yellow

t4.penup()
t5.penup()
t6.penup()

t4.goto(40,-45)
t5.goto(22,60)
t6.goto(-60,-10)

t4.pendown()
t5.pendown()
t6.pendown()

t1.ht()
t2.ht()
t3.ht()

t4.ht()
t5.ht()
t6.ht()

x = 5 #100
a = 90 #60

while True:
    t1.begin_fill()
    t2.begin_fill()
    t3.begin_fill()

    t1.circle(x,a)
    t2.circle(x,a)
    t3.circle(x,a)

    t1.circle(-x,a)
    t2.circle(-x,a)
    t3.circle(-x,a)

    t1.circle(2*x,a)
    t2.circle(2*x,a)
    t3.circle(2*x,a)

    t1.circle(5*-x,2*a)
    t2.circle(5*-x,2*a)
    t3.circle(5*-x,2*a)

    t1.end_fill()
    t2.end_fill()
    t3.end_fill()
    
    t1.rt(a/5.5) #3 #4
    t2.rt(a/5.5)
    t3.rt(a/5.5)
    
    
    t4.begin_fill()
    t5.begin_fill()
    t6.begin_fill()

    t4.circle(x/1.4,a)
    t5.circle(x/1.4,a)
    t6.circle(x/1.4,a)

    t4.circle(-x/1.4,a)
    t5.circle(-x/1.4,a)
    t6.circle(-x/1.4,a)

    t4.circle(2*x/1.4,a)
    t5.circle(2*x/1.4,a)
    t6.circle(2*x/1.4,a)

    t4.circle(5*-x/1.4,2*a)
    t5.circle(5*-x/1.4,2*a)
    t6.circle(5*-x/1.4,2*a)

    t4.end_fill()
    t5.end_fill()
    t6.end_fill()
    
    t4.rt(a/5.5) #3 #4
    t5.rt(a/5.5)
    t6.rt(a/5.5)
    
    a += 120 #75 #120
    
    if a > 360:
        a %= 360
