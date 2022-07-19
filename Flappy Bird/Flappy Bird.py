
import turtle
import os

f_alive = True
falling = True

os.chdir(os.getcwd())

s=turtle.getscreen()
turtle.title("Flappy Bird")
turtle.ht()

s.delay(1)

s.register_shape("flappyup.gif")
s.register_shape("flappydown.gif") 
s.register_shape("background1.gif")
s.register_shape("pipe30top.gif")
s.register_shape("pipe30bottom.gif")
s.register_shape("pipe20top.gif")
s.register_shape("pipe40bottom.gif")
s.register_shape("pipe40top.gif")
s.register_shape("pipe20bottom.gif")
s.register_shape("pipe15top.gif")
s.register_shape("pipe45bottom.gif")
s.register_shape("pipe15bottom.gif")
s.register_shape("pipe45top.gif")

fbackground = turtle.Turtle()
fbackground.shape("background1.gif")
fbackground.speed(0)
fbackground.penup()
fbackground.ht()

flappy = turtle.Turtle()
flappy.shape("flappyup.gif")
flappy.speed(0)
flappy.penup()
flappy.ht()

pipe30top = turtle.Turtle()
pipe30top.shape("pipe30top.gif")
pipe30top.speed(0)
pipe30top.penup()

pipe30bottom = turtle.Turtle()
pipe30bottom.shape("pipe30bottom.gif")
pipe30bottom.speed(0)
pipe30bottom.penup()

pipe40bottom = turtle.Turtle()
pipe40bottom.shape("pipe40bottom.gif")
pipe40bottom.speed(0)
pipe40bottom.penup()

pipe20top = turtle.Turtle()
pipe20top.shape("pipe20top.gif")
pipe20top.speed(0)
pipe20top.penup()

pipe40top = turtle.Turtle()
pipe40top.shape("pipe40top.gif")
pipe40top.speed(0)
pipe40top.penup()

pipe20bottom = turtle.Turtle()
pipe20bottom.shape("pipe20bottom.gif")
pipe20bottom.speed(0)
pipe20bottom.penup()

pipe15top = turtle.Turtle()
pipe15top.shape("pipe15top.gif")
pipe15top.speed(0)
pipe15top.penup()

pipe45bottom = turtle.Turtle()
pipe45bottom.shape("pipe45bottom.gif")
pipe45bottom.speed(0)
pipe45bottom.penup()

pipe15bottom = turtle.Turtle()
pipe15bottom.shape("pipe15bottom.gif")
pipe15bottom.speed(0)
pipe15bottom.penup()

pipe45top = turtle.Turtle()
pipe45top.shape("pipe45top.gif")
pipe45top.speed(0)
pipe45top.penup()

def Flap():
    if f_alive:
        global falling
        global t
        global v
        falling = False
        t = 0
        u1 = 44.27188724235731
        flappy.shape("flappydown.gif")
        for i in range(2):
            v1 = u1 - 9.8*t
            flappy.bk(v1)
            t+=1
        t = 0
        global u
        u = 10
        v = 0
        falling = True
        flappy.shape("flappyup.gif")

#start

flappy.rt(90)

def Start():
    fbackground.st()
    flappy.st()

    flappy.goto(-750,0)

    pipe30top.goto(0,300)
    pipe30bottom.goto(0,-300)
    pipe20top.goto(400,370)
    pipe40bottom.goto(400,-250)
    pipe40top.goto(800,250)
    pipe20bottom.goto(800,-370)
    pipe15top.goto(1200,470)
    pipe45bottom.goto(1200,-150)
    pipe15bottom.goto(1650,-450)
    pipe45top.goto(1650,170)

    turtle.listen()
    turtle.onkeypress(Flap," ")
    
    global t
    t = 0
    global u
    u = 10
    global f_alive
    f_alive = True

Start()
while True:
    while f_alive:
        
        pipe30top.setx(pipe30top.xcor()-10)
        pipe30bottom.setx(pipe30bottom.xcor()-10)
        pipe20top.setx(pipe20top.xcor()-10)
        pipe40bottom.setx(pipe40bottom.xcor()-10)
        pipe40top.setx(pipe40top.xcor()-10)
        pipe20bottom.setx(pipe20bottom.xcor()-10)
        pipe15top.setx(pipe15top.xcor()-10)
        pipe45bottom.setx(pipe45bottom.xcor()-10)
        pipe45top.setx(pipe45top.xcor()-10)
        pipe15bottom.setx(pipe15bottom.xcor()-10)
        
        t+=0.025
        if falling:
            v = u + 10*t
            #flappy.sety(flappy.ycor()-v)
            flappy.fd(v)
            u = v
        
        if pipe30top.xcor()<-1100:
            pipe30top.ht()
            pipe30bottom.ht()
            pipe30top.setx(pipe30top.xcor()+2100)
            pipe30bottom.setx(pipe30bottom.xcor()+2100)
            pipe30bottom.st()
            pipe30top.st()
            
        if pipe20top.xcor()<-1100:
            pipe20top.ht()
            pipe40bottom.ht()
            pipe20top.setx(pipe20top.xcor()+2100)
            pipe40bottom.setx(pipe40bottom.xcor()+2100)
            pipe40bottom.st()
            pipe20top.st()
        
        if pipe40top.xcor()<-1100:
            pipe40top.ht()
            pipe20bottom.ht()
            pipe40top.setx(pipe40top.xcor()+2100)
            pipe20bottom.setx(pipe20bottom.xcor()+2100)
            pipe20bottom.st()
            pipe40top.st()
        
        if pipe15top.xcor()<-1100:
            pipe15top.ht()
            pipe45bottom.ht()
            pipe15top.setx(pipe15top.xcor()+2100)
            pipe45bottom.setx(pipe45bottom.xcor()+2100)
            pipe45bottom.st()
            pipe15top.st()
        
        if pipe45top.xcor()<-1100:
            pipe45top.ht()
            pipe15bottom.ht()
            pipe45top.setx(pipe45top.xcor()+2100)
            pipe15bottom.setx(pipe15bottom.xcor()+2100)
            pipe15bottom.st()
            pipe45top.st()
          
        
        if -630>pipe30top.xcor()>-870 and (flappy.ycor()<-70 or flappy.ycor()>69):
            f_alive = False
        
        if -630>pipe20top.xcor()>-870 and (flappy.ycor()<69 or flappy.ycor()>215):
            f_alive = False
        
        if -630>pipe40top.xcor()>-870 and (flappy.ycor()<-210 or flappy.ycor()>-65):
            f_alive = False
        
        if -630>pipe15top.xcor()>-870 and (flappy.ycor()<100 or flappy.ycor()>360):
            f_alive = False
            
        if -630>pipe45top.xcor()>-870 and (flappy.ycor()>-100 or flappy.ycor()<-350):
            f_alive = False
        
        if flappy.ycor()<-500 or flappy.ycor()>500:
            f_alive = False
        
        s.update()

    else:
        Start()
