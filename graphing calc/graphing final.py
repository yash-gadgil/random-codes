
from turtle import *
from math import *

s = Screen()
t = Turtle()
t.speed(0)
s.delay(0)

f = textinput('Graphing Calc', 'Enter a function')

f1 = ''
for a,i in enumerate(f[::-1]):
    if i == 'x':
        try:
            int(f[::-1][a + 1])
            f1 += 'x*'
        except:
            f1 += 'x'
        continue
    f1 += '**' if i == '^' else i
f1 = f1[::-1]

a, b = -10, 10
for i in range(a,b + 1):
    if i == a: t.pu()
    t.goto(i,eval(f1.replace('x','('+str(i)+')')))
    if i == a: t.pd()

mainloop()
'''
#f = input('Enter a function: ')
#print(f2,eval(f2)) 
order, b = '', 0
for i in f:
    if i == ')': b = 0
    if i == '(' or b: b = 1
    if i in '-+x' and not b: order += i
print(order)
for i in order:
    pass
'''
