
from turtle import *
from os import *
import tkinter

info = tkinter.Tk()
screen_width = info.winfo_screenwidth()
screen_height = info.winfo_screenheight()
info.destroy()

files_path = getcwd()
chdir(files_path)

s = Screen()
s.delay(0)

s.register_shape("enemy.gif")
s.register_shape("enemyup.gif")
s.register_shape("enemydown.gif")
s.register_shape("enemyleft.gif")

allo = 500
setting = True
offsetx = 525    #540
offsety = 240

class screenchanger(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
    
    def up(self,x,y):
        global height, allo
        
        self.sety(max(0,min(y,(screen_height/2 + allo))))

        height = 2*(y + 68)

        #downpos = -y + 8 
        #t3.goto(0,downpos)

    def down(self,x,y):
        global height, allo
        
        self.sety(max((-screen_height/2 - allo),min(y,0)))

        height = 2*(-y + 76)

        uppos = -y + 8
        t2.goto(0,uppos)

    def left(self,x,y):
        global width, allo, offsetx
        
        self.setx(max(-screen_width/2 - allo,min(x,0)))

        offsetx += s.window_width() - 2*(-x + 69)

        width = 2*(-x + 69)

        #rightpos = -x - 8
        #t1.goto(rightpos,0)

    def right(self,x,y):
        global width, allo, offsetx
        
        self.setx(max(0,min(x,screen_width/2 + allo)))

        #offsetx -= s.window_width() - 2*(x + 77)

        width = 2*(x + 77)

        leftpos = -(x + 8)
        t4.goto(leftpos,0)

def Set():
    global setting

    setting = False

    t1.ht()
    t2.ht()
    t3.ht()
    t4.ht()

t1 = screenchanger()
t2 = screenchanger()
t3 = screenchanger()
t4 = screenchanger()

t1.shape("enemy.gif")
t2.shape("enemyup.gif")
t3.shape("enemydown.gif")
t4.shape("enemyleft.gif")

t1.goto(323,0)
t2.goto(0,282)
t3.goto(0,-274)
t4.goto(-331,0)

width, height = 800, 700

setup(width = 800, height = 700)

listen()
t1.ondrag(t1.right)
t2.ondrag(t2.up)
t3.ondrag(t3.down)
t4.ondrag(t4.left)

onkeypress(Set,"Return") # Return is key symbol for Enter

while setting:
    print(width,height, offsetx)

    setup(width = width, height = height, startx = offsetx, starty = offsety)
    
    s.update()
