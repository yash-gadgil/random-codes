
import turtle

s=turtle.getscreen()
turtle.title("graphing calc")
turtle.ht()

t = turtle.Turtle()
t.ht()

ffff = turtle.Turtle()
t.ht()


y = 0
k = 1
zoomed = 100
xcor = 0

def func(x):
    global y
    y = 1/5*x**2 
    return y

def zoomin():
    t.clear()
    global k
    global zoomed
    
    if k == 1:
        k+=1
    
    t.penup()
    t.goto(-11*k+xcor,func(-11*k))
    t.pendown()
    
    for i in range(-11,(10+1)):
        t.goto((i*k)+xcor,func((i*k)+xcor))
    k+=2
    zoomed+=20

def right():
    t.clear()
    
    global xcor
    xcor+=10
    
    t.penup()
    t.goto((-11*k)+xcor,func(-11*k))
    t.pendown()
    
    for j in range(-11*k,(10+1)*k):
        t.goto(j+xcor,func(j))
    #print("xcor =",xcor,"going to xcor =",(-11*k)+xcor,"going to ycor =",func((-11*k)+xcor))   


t.penup()
t.goto(-11,func(-11))
t.pendown()

for i in range(-11,10+1):
    t.goto(i,func(i))



while True:
    turtle.listen()
    turtle.onkeypress(zoomin,"z")
    turtle.onkeypress(right,"6")
    s.update()
