import turtle

s=turtle.getscreen()
#s.delay(0)
turtle.title("Triangle Maker")
turtle.ht()

t = turtle.Turtle()
t.penup()
t.ht()
t.speed(0)

#s.bgcolor("black")

p1 = turtle.Turtle()
p1.speed(0)
p1.penup()
p1.shape("circle")
p1.shapesize(0.5,0.5)
p1.ht()

p2 = turtle.Turtle()
p2.speed(0)
p2.penup()
p2.shape("circle")
p2.shapesize(0.5,0.5)
p2.ht()

p3 = turtle.Turtle()
p3.speed(0)
p3.penup()
p3.shape("circle")
p3.shapesize(0.5,0.5)
p3.pensize(2)
p3.fillcolor("black")
p3.ht()

tm = turtle.Turtle()
tm.speed(0)
tm.penup()
tm.pensize(2)
tm.fillcolor("white")
tm.ht()

points = 0

def dragged(x,y):
    global points
    t.goto(x,y)
    if points == 0:
        p3.clear()
        tm.clear()
        p1.ht()
        p2.ht()
        p3.ht()
        p3.penup()
        p1.goto(t.pos())
        p1.st()
        points+=1
    elif points == 1:
        p2.goto(t.pos())
        p2.st()
        points+=1
    elif points == 2:
        p3.goto(p1.pos())
        p3.pendown()
        p3.begin_fill()
        p3.goto(p2.pos())
        p3.goto(t.pos())
        p3.goto(p1.pos())
        p3.end_fill()
        p3.goto(t.pos())
        p3.st()
        
        #middle tri
        m1x = ( p1.xcor() + p2.xcor() )/2
        m1y = ( p1.ycor() + p2.ycor() )/2
        
        tm.goto(m1x,m1y)
        tm.pendown()
        tm.begin_fill()
        
        m2x = ( p2.xcor() + p3.xcor() )/2
        m2y = ( p2.ycor() + p3.ycor() )/2
        
        tm.goto(m2x,m2y)
        
        m3x = ( p3.xcor() + p1.xcor() )/2
        m3y = ( p3.ycor() + p1.ycor() )/2
        
        tm.goto(m3x,m3y)
        tm.end_fill()
        tm.goto(m1x,m1y)
        tm.penup()
        
        #top mid tri
        m1x2 = ( m1x + p2.xcor() )/2
        m1y2 = ( m1y + p2.ycor() )/2
        
        tm.goto(m1x2,m1y2)
        tm.pendown()
        tm.begin_fill()
        
        m2x2 = ( p2.xcor() + m2x )/2
        m2y2 = ( p2.ycor() + m2y )/2
        
        tm.goto(m2x2,m2y2)
        
        m3x2 = ( m2x + m1x )/2
        m3y2 = ( m2y + m1y )/2
        
        tm.goto(m3x2,m3y2)
        tm.end_fill()
        tm.goto(m1x2,m1y2)
        tm.penup()
        
        #left mid tri
        m1x3 = ( p1.xcor() + m1x )/2
        m1y3 = ( p1.ycor() + m1y )/2
        
        tm.goto(m1x3,m1y3)
        tm.pendown()
        tm.begin_fill()
        
        m2x3 = ( m1x + m3x )/2
        m2y3 = ( m1y + m3y )/2
        
        tm.goto(m2x3,m2y3)
        
        m3x3 = ( m3x + p1.xcor() )/2
        m3y3 = ( m3y + p1.ycor() )/2
        
        tm.goto(m3x3,m3y3)
        tm.end_fill()
        tm.goto(m1x3,m1y3)
        tm.penup()
        
        #right mid tri
        m1x4 = ( m3x + m2x )/2
        m1y4 = ( m3y + m2y )/2
        
        tm.goto(m1x4,m1y4)
        tm.pendown()
        tm.begin_fill()
        
        m2x4 = ( m2x + p3.xcor() )/2
        m2y4 = ( m2y + p3.ycor() )/2
        
        tm.goto(m2x4,m2y4)
        
        m3x4 = ( m3x + p3.xcor() )/2
        m3y4 = ( m3y + p3.ycor() )/2
        
        tm.goto(m3x4,m3y4)
        tm.end_fill()
        tm.goto(m1x4,m1y4)
        tm.penup()
        
        #top top tri
        m1x5 = ( m1x2 + p2.xcor() )/2
        m1y5 = ( m1y2 + p2.ycor() )/2
        
        tm.goto(m1x5,m1y5)
        tm.pendown()
        tm.begin_fill()
        
        m2x5 = ( p2.xcor() + m2x2 )/2
        m2y5 = ( p2.ycor() + m2y2 )/2
        
        tm.goto(m2x5,m2y5)
        
        m3x5 = ( m2x2 + m1x2 )/2
        m3y5 = ( m2y2 + m1y2 )/2
        
        tm.goto(m3x5,m3y5)
        tm.end_fill()
        tm.goto(m1x5,m1y5)
        tm.penup()
        
        #top left tri
        m1x6 = ( m1x + m1x2 )/2
        m1y6 = ( m1y + m1y2 )/2
        
        tm.goto(m1x6,m1y6)
        tm.pendown()
        tm.begin_fill()
        
        m2x6 = ( m1x2 + m3x2 )/2
        m2y6 = ( m1y2 + m3y2 )/2
        
        tm.goto(m2x6,m2y6)
        
        m3x6 = ( m3x2 + m1x )/2
        m3y6 = ( m3y2 + m1y )/2
        
        tm.goto(m3x6,m3y6)
        tm.end_fill()
        tm.goto(m1x6,m1y6)
        tm.penup()
        
        #top right tri
        m1x7 = ( m3x2 + m2x2 )/2
        m1y7 = ( m3y2 + m2y2 )/2
        
        tm.goto(m1x7,m1y7)
        tm.pendown()
        tm.begin_fill()
        
        m2x7 = ( m2x2 + m2x )/2
        m2y7 = ( m2y2 + m2y )/2
        
        tm.goto(m2x7,m2y7)
        
        m3x7 = ( m2x + m3x2 )/2
        m3y7 = ( m2y + m3y2 )/2
        
        tm.goto(m3x7,m3y7)
        tm.end_fill()
        tm.goto(m1x7,m1y7)
        tm.penup()
        
        #left top tri
        m1x8 = ( m1x3 + m1x )/2
        m1y8 = ( m1y3 + m1y )/2
        
        tm.goto(m1x8,m1y8)
        tm.pendown()
        tm.begin_fill()
        
        m2x8 = ( m1x + m2x3 )/2
        m2y8 = ( m1y + m2y3 )/2
        
        tm.goto(m2x8,m2y8)
        
        m3x8 = ( m2x3 + m1x3 )/2
        m3y8 = ( m2y3 + m1y3 )/2
        
        tm.goto(m3x8,m3y8)
        tm.end_fill()
        tm.goto(m1x8,m1y8)
        tm.penup()
        
        #left left tri
        m1x9 = ( p1.xcor() + m1x3 )/2
        m1y9 = ( p1.ycor() + m1y3 )/2
        
        tm.goto(m1x9,m1y9)
        tm.pendown()
        tm.begin_fill()
        
        m2x9 = ( m1x3 + m3x3 )/2
        m2y9 = ( m1y3 + m3y3 )/2
        
        tm.goto(m2x9,m2y9)
        
        m3x9 = ( m3x3 + p1.xcor() )/2
        m3y9 = ( m3y3 + p1.ycor() )/2
        
        tm.goto(m3x9,m3y9)
        tm.end_fill()
        tm.goto(m1x9,m1y9)
        tm.penup()
        
        #left right tri
        m1x10 = ( m3x3 + m2x3 )/2
        m1y10 = ( m3y3 + m2y3 )/2
        
        tm.goto(m1x10,m1y10)
        tm.pendown()
        tm.begin_fill()
        
        m2x10 = ( m2x3 + m3x )/2
        m2y10 = ( m2y3 + m3y )/2
        
        tm.goto(m2x10,m2y10)
        
        m3x10 = ( m3x + m3x3 )/2
        m3y10 = ( m3y + m3y3 )/2
        
        tm.goto(m3x10,m3y10)
        tm.end_fill()
        tm.goto(m1x10,m1y10)
        tm.penup()
        
        #right top tri
        m1x11 = ( m1x4 + m2x )/2
        m1y11 = ( m1y4 + m2y )/2
        
        tm.goto(m1x11,m1y11)
        tm.pendown()
        tm.begin_fill()
        
        m2x11 = ( m2x + m2x4 )/2
        m2y11 = ( m2y + m2y4 )/2
        
        tm.goto(m2x11,m2y11)
        
        m3x11 = ( m2x4 + m1x4 )/2
        m3y11 = ( m2y4 + m1y4 )/2
        
        tm.goto(m3x11,m3y11)
        tm.end_fill()
        tm.goto(m1x11,m1y11)
        tm.penup()
        
        #right left tri
        m1x12 = ( m3x + m1x4 )/2
        m1y12 = ( m3y + m1y4 )/2
        
        tm.goto(m1x12,m1y12)
        tm.pendown()
        tm.begin_fill()
        
        m2x12 = ( m1x4 + m3x4 )/2
        m2y12 = ( m1y4 + m3y4 )/2
        
        tm.goto(m2x12,m2y12)
        
        m3x12 = ( m3x4 + m3x )/2
        m3y12 = ( m3y4 + m3y )/2
        
        tm.goto(m3x12,m3y12)
        tm.end_fill()
        tm.goto(m1x12,m1y12)
        tm.penup()
        
        #right right tri
        m1x13 = ( m3x4 + m2x4 )/2
        m1y13 = ( m3y4 + m2y4 )/2
        
        tm.goto(m1x13,m1y13)
        tm.pendown()
        tm.begin_fill()
        
        m2x13 = ( m2x4 + p3.xcor() )/2
        m2y13 = ( m2y4 + p3.ycor() )/2
        
        tm.goto(m2x13,m2y13)
        
        m3x13 = ( p3.xcor() + m3x4 )/2
        m3y13 = ( p3.ycor() + m3y4 )/2
        
        tm.goto(m3x13,m3y13)
        tm.end_fill()
        tm.goto(m1x13,m1y13)
        tm.penup()
        
        tm.penup()
        points = 0

turtle.listen()
s.onscreenclick(dragged)
