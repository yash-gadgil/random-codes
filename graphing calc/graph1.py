import turtle

s=turtle.getscreen()
turtle.title("graphing calc")
turtle.ht()

t = turtle.Turtle()
t.ht()

axis = turtle.Turtle()
axis.pencolor("red")
axis.ht()

axis.fd(450)
axis.bk(900)
axis.fd(450)
axis.lt(90)
axis.fd(450)
axis.bk(900)

startrange = -50
endrange = -startrange + 1
k = 1
zoomed = 100
xcor = 0

def func(x):
    global y
    y = 1/9*x**2 - 2*x + 25
    return y

def zoomin():
    t.clear()
    global k
    global zoomed
    
    if k == 1:
        k+=1
    
    t.penup()
    t.goto(startrange*k+xcor,func(startrange*k))
    t.pendown()
    
    for i in range(startrange,endrange):
        t.goto((i*k)+xcor,func(i*k))
    k+=4
    zoomed+=20

t.penup()
t.goto(startrange,func(startrange))
t.pendown()

for i in range(startrange,endrange):
    t.goto(i,func(i))
    
while True:
    turtle.listen()
    turtle.onkeypress(zoomin,"z")
    s.update()