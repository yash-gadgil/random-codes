
from turtle import *

s = Screen()

t_holder = {}
p = ["a1","s1","d1","f1","g1","h1"]

for i in p:

    t_holder[i] = Turtle()
    
locals().update(t_holder)

a1.goto(10,10)
