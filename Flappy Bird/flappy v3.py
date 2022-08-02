
'''
from turtle import *
from os import *
import traceback
import tkinter
from threading import Thread
from threaded_turtle import ThreadSerializer, TurtleThread

info = tkinter.Tk()
screen_width = info.winfo_screenwidth()
screen_height = info.winfo_screenheight()
info.destroy()

files_path = getcwd()
chdir(files_path)

f_alive = True
falling = True

u = 3
t = 0

s = Screen()
s.title("Flappy Bird 2.0")
#s.delay(.99999999)

s.register_shape("background1.gif")
s.register_shape("flappyup.gif")
s.register_shape("flappydown.gif")

background = Turtle()
background.shape("background1.gif")

flappy = Turtle()
flappy.shape("flappyup.gif")
flappy.speed(0)
flappy.pu()
flappy.rt(90)

pipes = []

class Pipes(Turtle):
    
    def __init__(self, def_name = None):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        
        if def_name == None:
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
        self.defined_name = def_name
        
        self.giveshape()
        pipes.append(self)
        
    def giveshape(self):
        shapename = self.defined_name +".gif"
        s.register_shape(shapename)
        self.shape(shapename)

pipe15top = Pipes()
pipe20top = Pipes()
pipe30top = Pipes()
pipe40top = Pipes()
pipe45top = Pipes()

pipe15bottom = Pipes()
pipe20bottom = Pipes()
pipe30bottom = Pipes()
pipe40bottom = Pipes()
pipe45bottom = Pipes()

def Flap():
    global f_alive
    if f_alive:
        global falling, t, v
        falling = False
        t = 0
        u1 = 44.27188724235731
        flappy.shape("flappydown.gif")
        for i in range(2):
            v1 = u1 - 9.8*t
            flappy.bk(v1)
            t+=1
            s.update()
        t = 0
        global u
        u = 10
        v = 0
        falling = True
        flappy.shape("flappyup.gif")


#threads = [Thread(target = pipe.setx, args = (pipe.xcor()-10,)) for pipe in pipes]
'''
'''
def thread_maker(pipe1):

    def pipemove(pipe1 = pipe1):
        pipe1.setx(pipe1.xcor()-10)

    return pipemove

threads = []
for pipe in pipes:
    f = thread_maker(pipe)
    threads.append(Thread( target = f))
'''
'''
def Motion():
    global t, u, v
    
    t += 0.015
    v = u + 10*t
    flappy.fd(v)
    u = v
    
    s.update()


'''
'''
threads.append(Thread(target = Motion))

#for pipe in pipes:
    #pipe.setx(pipe.xcor()-10)





    
#for thread in threads:
    #thread.start()

'''
'''
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
'''
'''
def pipemove():
    global stop
    while True:
        for pipe in pipes:
            pipe.setx(pipe.xcor()-10)
        if stop:
            break

t1 = Thread(target = pipemove)
t1.start()
def Start():
    
    
    flappy.goto(-screen_width/2.6,0)
    
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
    
    global t
    t = 0
    global u
    u = 10
    global f_alive
    f_alive = True
    global stop
    stop = False

Start()

listen()
onkeypress(Flap, "f")


while True:

    while f_alive:
        
        

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

        stop = True
        t1.join()
        Start()
        
'''

'''
from turtle import *
from threaded_turtle import ThreadSerializer, TurtleThread
from math import *

s = Screen()
s.delay(0)
ctrl = ThreadSerializer()                        ## <-- create a serializer

n = 12

#t1=Turtle()
#t2=Turtle()
d = [Turtle() for i in range(n)]
for i in range(n): d[i].lt(30*i)
    

def f_maker(turtle):

    def ff(t = turtle):
        t.speed(0)
        k = 0
        while k < 360:
            t.fd(1)
            t.lt(1)
            #t.circle(20,k)
            k += 1

    return ff

funcs = [f_maker(i) for i in d]

tfuncs = [(d[i],funcs[i]) for i in range(n)]

def tes1(t1):                                    ## <-- additional argument
  t1.speed(0)
  i=0
  while i < 360:
    t1.forward(3)
    t1.left(1)
    i+=1

def tes2(t2):                                    ## <-- additional argument
  t2.speed(0)
  i=0
  while i < 360:
    t2.forward(1)
    t2.right(1)
    i+=1
'''
'''
t = TurtleThread(ctrl, t1, target=tes1)          ## <-- additional arguments
t.daemon = True
t.start()

t3 = TurtleThread(ctrl, t2, target=tes2)         ## <-- additional arguments
t3.daemon = True
t3.start()
'''
'''
threads = [TurtleThread(ctrl, tfunc[0],target = tfunc[1]) for tfunc in tfuncs]
for thread in threads:
    thread.daemon = True
    thread.start()
while True:
    
    for thread in threads:
        if not thread.is_alive():
            thread.start()

        


ctrl.run_forever(1)
'''
'''
from turtle import *
from os import *
import traceback
import tkinter
from threaded_turtle import ThreadSerializer, TurtleThread

info = tkinter.Tk()
screen_width = info.winfo_screenwidth()
screen_height = info.winfo_screenheight()
info.destroy()

files_path = getcwd()
chdir(files_path)

f_alive = True
falling = True

u = 3
t = 0

s = Screen()
s.title("Flappy Bird 2.0")
s.delay(0)

s.register_shape("background1.gif")
s.register_shape("flappyup.gif")
s.register_shape("flappydown.gif")

background = Turtle()
background.shape("background1.gif")

flappy = Turtle()
flappy.shape("flappyup.gif")
flappy.speed(1)
flappy.pu()
flappy.rt(90)

pipes = []

class Pipes(Turtle):
    
    def __init__(self, def_name = None):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        
        if def_name == None:
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
        self.defined_name = def_name
        
        self.giveshape()
        pipes.append(self)
        
    def giveshape(self):
        shapename = self.defined_name +".gif"
        s.register_shape(shapename)
        self.shape(shapename)

pipe15top = Pipes()
pipe20top = Pipes()
pipe30top = Pipes()
pipe40top = Pipes()
pipe45top = Pipes()

pipe15bottom = Pipes()
pipe20bottom = Pipes()
pipe30bottom = Pipes()
pipe40bottom = Pipes()
pipe45bottom = Pipes()

def Start():
    
    flappy.goto(-screen_width/2.6,0)
    
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
    
    global t
    t = 0
    global u
    u = 10
    global f_alive
    f_alive = True

def Flap():
    global f_alive, falling, t, v, u
    if f_alive:
        falling = False
        t = 0
        u1 = 44.27188724235731
        flappy.shape("flappydown.gif")
        for i in range(2):
            v1 = u1 - 9.8*t
            flappy.bk(v1)
            t+=1
            s.update()
        t = 0
        u = 5 #10
        v = 0
        falling = True
        flappy.shape("flappyup.gif")

def Motion(x):
    global t, u, v, f_alive
    
    #t += 0.015
    v = u + 0.4# u + 10*t
    flappy.fd(v)
    u = v
    
     #10 #Motion()
    
    s.update()

    if f_alive:
        ontimer(Motion, t = 200)
    else:
        Start()
    

ctrl = ThreadSerializer()




Start()

t1 = TurtleThread(ctrl, flappy, target= Motion)
t1.daemon = True
t1.start()

listen()
onkeypress(Flap, "f")

ctrl.run_forever(1)
while True:

    while f_alive:
        

        for pipe in pipes:
            pipe.setx(pipe.xcor()-9)

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
'''


from turtle import *
from threaded_turtle import ThreadSerializer, TurtleThread

s = Screen()
t = Turtle()

li = [Turtle() for i in range(3)]
[i.speed(0) for i in li]
[i[1].goto(0,10*(i[0] + 1)) for i in enumerate(li)]

s.delay(0)
t.speed(0)

g, ff = 0, True

c = ThreadSerializer()

#def

def lis(h):
    h.fd(1)
    #for i in li:
        #i.fd(3)
    lis(h)
    

def move(t):
    global g, ff

    if ff:
        g += 1

        t.fd(1)
        print(g)
    else:
        print(ff)
    move(t)

def fff():
    global ff
    ff = not ff

t1 = TurtleThread(c, t,target= move)
t1.daemon = True
t1.start()

#t2 = TurtleThread(c, li[0], target= lis)
#t2.daemon = True
#t2.start()

#listen()
#onkeypress(fff, "f")



while True:
    #g += 1
    if g > 200:
        break
    print(g)

c.run_forever(1)




