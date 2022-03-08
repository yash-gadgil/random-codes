import turtle

s=turtle.getscreen()
turtle.title("Shuriken")
turtle.ht()
#s.bgcolor("black")
s.bgcolor("white")
s.delay(0)

t1 = turtle.Turtle()
t1.speed(6)
t1.pensize(3)
t1.fillcolor("#891300")

'''
t2 = turtle.Turtle()
t2.speed(0)
t2.pensize(3)
t2.fillcolor("#891300")
#t2.ht()
'''

x = 5
a1 = 15
a2 = 0

t1.penup()
t1.goto(0,100)
t1.pendown()


'''
t2.penup()
t2.goto(54,-14)
t2.pendown()

t2.lt(29)
'''

while True:
    
    t1.begin_fill()
    
    t1.fd(2*x)
    t1.lt(2*a1)
    
    t1.fd(x)
    t1.lt(a1)
    
    t1.fd(2*x)
    t1.lt(2*a1)
    
    t1.fd(x)
    t1.lt(a1)
    
    t1.fd(2*x)
    t1.lt(2*a1)
    
    t1.end_fill()
    
    a1 += 1
    
#a1 %= 5.11 #5.11

#t2.fd(x)
#t2.lt(a2)

#a2 += 155
    
'''
t2.begin_fill()

t2.fd(x/3.4)
t2.lt(a1)

t2.fd(2*x/3.4)
t2.lt(2*a1)

t2.fd(x/3.4)
t2.lt(a1)

t2.end_fill()
'''
    
