
#import pickle


'''
with open('savefile.txt','r+') as f:
    f.write("\n[1,2,3,4,5]")
    f.write("\n[123, 624, 662, 136]")
    li = [eval(i.replace('\n','')) for i in f.readlines()]
    print(li)
'''

from turtle import *

s = Screen()
s.delay(0)

t = Turtle()
t.speed(0)
t.pu()


with open('savefile.txt','r') as f:
    d = eval(f.read().replace('\n',''))

t.goto(d['location'])

def up():
    t.sety(t.ycor() + 50)
def down():
    t.sety(t.ycor() - 50)
def left():
    t.setx(t.xcor() - 50)
def right():
    t.setx(t.xcor() + 50)
def save():
    with open('savefile.txt','w') as f:
        f.write('{"location" : ' + str(t.pos()) + '}')


listen()
onkeypress(up,"w")
onkeypress(down,"s")
onkeypress(right,"d")
onkeypress(left,"a")
onkeypress(save,"x")

