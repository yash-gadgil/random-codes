import turtle

s=turtle.getscreen()
turtle.title("Shuriken")
turtle.ht()
#s.bgcolor("black")
s.bgcolor("white")

t1 = turtle.Turtle()
t1.speed(0)
t1.pensize(3)
t1.fillcolor("#891300") #red

t2 = turtle.Turtle()
t2.speed(0)
t2.lt(90)
t2.pensize(3)
t2.fillcolor("#0D98BA") #green

t3 = turtle.Turtle()
t3.speed(0)
t3.lt(180)
t3.pensize(3)
t3.fillcolor("#00FFFF") #blue

t4 = turtle.Turtle()
t4.speed(0)
t4.rt(90)
t4.pensize(3)
t4.fillcolor("#FDDA0D") #yellow

t1.ht()
t2.ht()
t3.ht()
t4.ht()

x = 45
a = 386 

while True:

    t1.begin_fill()
    t2.begin_fill()
    t3.begin_fill()
    t4.begin_fill()

    t1.fd(x)
    t2.fd(x)
    t3.fd(x)
    t4.fd(x)

    t1.lt(a/2)
    t2.lt(a/2)
    t3.lt(a/2)
    t4.lt(a/2)

    t1.fd(x)
    t2.fd(x)
    t3.fd(x)
    t4.fd(x)

    t1.lt(a)
    t2.lt(a)
    t3.lt(a)
    t4.lt(a)

    t1.bk(x)
    t2.bk(x)
    t3.bk(x)
    t4.bk(x)

    t1.lt(a/2)
    t2.lt(a/2)
    t3.lt(a/2)
    t4.lt(a/2)

    t1.fd(2*x)
    t2.fd(2*x)
    t3.fd(2*x)
    t4.fd(2*x)

    t1.end_fill()
    t2.end_fill()
    t3.end_fill()
    t4.end_fill()
    
    a-=30

'''
while True:
    
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
    t1.circle(x/a,a,3)
    t1.lt(a)
    t2.circle(x/a,a,3)
    t2.lt(a)
    t3.circle(x/a,a,3)
    t3.lt(a)
    t4.circle(x/a,a,3)
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
'''
t1.begin_fill()
t2.begin_fill()
t3.begin_fill()
t4.begin_fill()
'''
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

t1.circle(x,a)
t1.lt(a)
t2.circle(x,a)
t2.lt(a)
t3.circle(x,a)
t3.lt(a)
t4.circle(x,a)
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

t1.circle(a,x)
t1.lt(a)
t2.circle(a,x)
t2.lt(a)
t3.circle(a,x)
t3.lt(a)
t4.circle(a,x)
t4.lt(a)

a+=90 #135 #135 #45 #45 #60 #1 #3

'''