import turtle
func=input("Enter a polynomial function: ")

r1=int(input("Enter the lower limit of the range: "))
r2=int(input("Enter the upper limit of the range: "))

s=turtle.getscreen()
turtle.title("graph")
t=turtle.Turtle()
turtle.ht()
t.pensize(1)


def function(x):
    y=int(x**2)
    t.goto(x,y)

t.speed(0)
t.pencolor("red")
t.fd(150)
t.bk(300)
t.fd(150)
t.lt(90)
t.fd(150)
t.bk(300)
t.fd(150)

t.pencolor("black")
t.penup()
t.goto(r1,r1**2)
t.pendown()

t.speed(0)
for i in range(r1,r2+100):
    function(i)