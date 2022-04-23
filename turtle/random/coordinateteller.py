import turtle

s=turtle.getscreen()
s.delay(0)
turtle.title("Coordinate Marker")
turtle.ht()

t = turtle.Turtle()
turtle.ht()
t.penup()
t.ht()
t.speed(0)
t.shape("circle")
t.shapesize(0.1,0.1)

write = turtle.Turtle()
write.penup()
write.ht()
write.speed(0)

def dragged(x,y):
    write.clear()
    t.ht()
    t.goto(x,y)
    write.goto(t.pos())
    if t.ycor()<485:
        if t.xcor()>885:
            write.sety(write.ycor()+10)
            write.setx(write.xcor()-60)
        else:
            write.sety(write.ycor()+10)
    else:
        if t.xcor()>885:
            write.sety(write.ycor()-10)
            write.setx(write.xcor()-60)
        else:
            write.sety(write.ycor()-10)
    write.write(str(t.pos()))
    t.st()

turtle.listen()
s.onscreenclick(dragged)
turtle.mainloop()
