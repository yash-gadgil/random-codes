import turtle

s=turtle.getscreen()
turtle.title("Triangle Maker")
turtle.ht()
s.bgcolor("grey")

t1 = turtle.Turtle()
t1.speed(0)
t1.pensize(3)
t1.fillcolor("red")

t2 = turtle.Turtle()
t2.speed(0)
t2.lt(90)
t2.pensize(3)
t2.fillcolor("green")

t3 = turtle.Turtle()
t3.speed(0)
t3.lt(180)
t3.pensize(3)
t3.fillcolor("blue")

t4 = turtle.Turtle()
t4.speed(0)
t4.rt(90)
t4.pensize(3)
t4.fillcolor("yellow")

x = 100
a = 90


t1.ht()
t2.ht()
t3.ht()
t4.ht()

t1.begin_fill()
t1.fd(x)
t1.lt(a)

t2.begin_fill()
t2.fd(x)
t2.lt(a)

t3.begin_fill()
t3.fd(x)
t3.lt(a)

t4.begin_fill()
t4.fd(x)
t4.lt(a)

t1.fd(x)
t1.lt(a)
t2.fd(x)
t2.lt(a)
t3.fd(x)
t3.lt(a)
t4.fd(x)
t4.lt(a)
t1.fd(x)
t1.lt(a)
t2.fd(x)
t2.lt(a)
t3.fd(x)
t3.lt(a)
t4.fd(x)
t4.lt(a)

t1.fd(x)
t1.lt(a)
t2.fd(x)
t2.lt(a)
t3.fd(x)
t3.lt(a)
t4.fd(x)
t4.lt(a)

t1.end_fill()
t2.end_fill()
t3.end_fill()
t4.end_fill()

'''
t1.begin_fill()
t2.begin_fill()
t3.begin_fill()
t4.begin_fill()
'''

t1.bk(2*x)
t1.lt(a)
t2.bk(2*x)
t2.lt(a)
t3.bk(2*x)
t3.lt(a)
t4.bk(2*x)
t4.lt(a)

t1.begin_fill()
t2.begin_fill()
t3.begin_fill()
t4.begin_fill()

t1.fd(2*x)
t1.lt(a)
t2.fd(2*x)
t2.lt(a)
t3.fd(2*x)
t3.lt(a)
t4.fd(2*x)
t4.lt(a)

t1.bk(2*x)
t1.lt(a)
t2.bk(2*x)
t2.lt(a)
t3.bk(2*x)
t3.lt(a)
t4.bk(2*x)
t4.lt(a)

t1.end_fill()
t2.end_fill()
t3.end_fill()
t4.end_fill()
