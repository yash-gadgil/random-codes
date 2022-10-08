

from turtle import *
from os import *
from random import *
from math import *
#from time import *
#from datetime import *

chdir(getcwd())

s = Screen()
s.title("Clash Demo")
s.register_shape("chasercrab.gif")
s.register_shape("enemy1.gif")
s.register_shape("anda1.gif")

f00d = []
eggs = []
crabs = []
d = {}

def isneg(n): return n<0
def ispos(n): return n>0
def iszero(n): return n==0

class food(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.pu()
        self.shape("enemy1.gif")
        self.goto(randint(-500,500),randint(-500,500))
        f00d.append(self)

class egg(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(3)
        self.pu()
        self.ht()
        self.shape("anda1.gif")
        #self.goto(randint(-500,500),randint(-500,500))
        eggs.append(self)
        self.laid = False

    def hatch(self):

        '''
        start = datetime.now()
        t = 0
        while t <= 3.0:
            stop = datetime.now()
            t = (stop - start).total_seconds()
        '''
        
        h = Crab()
        h.ht()
        h.goto(self.pos())
        h.st()
        self.ht()
        eggs.remove(self)

'''
    def runaway(self):

        proxim, closest, proxim1 = [], 1000, []

        for a,crab in enumerate(crabs):
            if abs(abs(crab.xcor()) - abs(self.xcor())) <= 15/sqrt(2) and abs(abs(crab.ycor()) - abs(self.ycor())) <= 15/sqrt(2):
                proxim.append(sqrt(abs(abs(crab.xcor()) - abs(self.xcor()))**2 + abs(abs(crab.ycor()) - abs(self.ycor()))**2))
                proxim1.append(a)

        x, x1 = crabs[proxim1[proxim.index(min(proxim))]].xcor(), self.xcor()
        
        #x += 15/sqrt(2) if (abs(x) > abs(x1) and isneg(x) and not ispos(x1)) or (abs(x) < abs(x1) and not isneg(x) and ispos(x1)) or () else ()
'''

class Crab(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(5)
        self.pu()
        self.shape("chasercrab.gif")
        crabs.append(self)
        
    def walk(self):
        for i in range(20):
            self.lt(randint(0,90)) if randint(0,1) else self.rt(randint(0,90))
            self.fd(30)

    def eat(self):
        
        proxim, proxim1 = [], []
        try:
            for a,morsel in enumerate(f00d):
                proxim.append(sqrt(abs(morsel.xcor() - self.xcor())**2 + abs(morsel.ycor() - self.ycor())**2))
                proxim1.append(a)
                
            foodno = proxim1[proxim.index(min(proxim))]
                    
            #l = randint(0,len(f00d)-1)
            #self.goto(f00d[l].pos())
            self.goto(f00d[foodno].pos())
            f00d[foodno].ht()
            f00d.pop(foodno)
        except: pass

    def lay(self):

        try:
            for i in eggs:
                if not i.laid:
                    i.goto(self.pos())
                    i.st()
                    i.laid = True
                    break
        except: pass

def egghatch():
    for egg in eggs:
        if egg.laid:
            egg.hatch()
            break


t = Crab()

'''
e = food()
f = food()
h = food() 
eg = egg()
'''


for i in range(3): d[i] = egg()
for i in range(3): d[i] = food()

#def tw(): t.walk()

listen()
onkeypress(t.walk,"w")
onkeypress(t.eat,"e")
onkeypress(t.lay,"l")
onkeypress(egghatch,"h")









