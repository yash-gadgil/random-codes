#1
'''
num = float(input("Enter a number: "))  
if num > 0:
    print("It is a positive number")     
else:
    print("It is a negative number")

#2
    
num = float(input("Enter a number: "))
if num%2==0:
    print("It is an even number")
else:
    print("It is an odd number")

#3
    
num = float(input("Enter a number: "))
if num%2==0:
    print("the square is ",num*num)
else:
    print("the cube is ",num*num*num)

#4
    
day=input("Enter a day: ")
if day=="Friday" or day=="Saturday":
    print("Holiday")
else:
    print("Working Day")

#5
    
num = float(input("Enter a number: "))  
if num > 0:
    print("It is a positive number")  
elif num == 0:
    print("It is zero")   
else:
    print("It is a negative number")

#6

num=float(input("enter the 4 digit number"))
if num%100==0 and num%400==0:
    print("It is a leap year")
elif num%100!=0 and num%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")

#7

length = float(input ("Enter length"))
breadth = float(input ("Enter breath"))
Perimeter = 2*(length+breadth)
area=length*breadth
if area>Perimeter:
    print ("Area is larger than its perimeter")
elif perimeter>area:
    print("Area is smaller than its perimeter")
else:
    print ("Area and Perimeter are equal")

#8

u= int(input("Enter first number "))
d= int(input("Enter second number "))
t= int(input("Enter third number "))
if u>d and u>t:
    print ("The largest number is ",u)
elif d>u and d>t:
    print ("The largest number is ",d)
else:
    print("The largest number is ",t)

#9

s=int(input("Enter the Sales "))
if s>50000:
    d=(40/100)*s
elif s>40001:
    d=(30/100)*s
elif sales>30001:
    d=(20/100)*s
elif sales>20001:
    d=(15/100)*s
else:
    d=(5/100)*s
n=s-d
print ("Net amount is ",n)

#10

u=int(input("Enter the first number"))
d=int(input("Enter the second number"))
o=input("Enter operator")
if o=="+":
    print(u+d)
elif o=="-":
    print(u-d)
elif o=="*":
    print(u*d)
elif o=="/":
    print(u/d)
elif o=="%":
    print(u%d)
    
#11
    
d=input("Enter the day ")
if d=="Saturday" or d=="saturday" or d=="Thursday" or d=="thursday":
    print("The entrance fee is 5Dhs")
elif d=="Sunday" or d=="sunday" or d=="Friday" or d=="friday":
    print("The entrance fee is 4Dhs")
elif d=="Monday" or d=="monday":
    print("The entrance fee is 3Dhs")
elif d=="Tuesday" or d=="tuesday" or d=="Wednesday" or d=="wednesday":
    print("The entrance fee is 2Dhs")
    
#12
    
p=int(input("Enter Phy marks "))
c=int(input("Enter Chem marks "))
m=int(input("Enter Math marks "))
a=(p+c+m)/300*100
if a>90:
    print("Grade=A")
elif a>81:
    print("Grade=B")
elif a>71:
    print("Grade=C")
else:
    print("Grade=D")
 
#13
    
d=int(input("Enter the day of the month"))
m=int(input("Enter the month no."))
y=int(input("Enter the year"))
if m==1:
    if d==1:
        print("The Date is",d,"th January",y)

#14

import math
print("enter the coefficients for the quadratic equation ax^2+bx+c=0")
a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
c=float(input("enter the value of c: "))
d=(b**2)-(4*a*c)
if d>0:
    r1=(-b+(math.sqrt(d)))/(2*a)
    r2=(-b-(math.sqrt(d)))/(2*a)
    print("1st root is",r1,"2nd root is",r2)
elif d==0:
    r=-b/(2*a)
    print("the root is",r)
elif d<0:
    print("there are no real roots")
  '''
'''
#15

print("\tMAIN MENU\n------------------------\nArea of a Triangle\nArea of a Square\nArea of a Circle\nExit")
op=input("Enter which option you want to select")
'''
'''
from turtle import *

s = Screen()
t = Turtle()
t.pensize(3)
t.fillcolor("white")

x = 50

t.fd(100)

t.lt(90)
t.fd(10)


t.circle(x,90)
t.circle(x,90)


t.fd(10)
#t.rt(150)
#t.circle(35,162)
'''

from turtle import *

s = Screen()
f = []

d = {(0, 0): (-350.0, 350.0), (1, 0): (-262.5, 350.0), (2, 0): (-175.0, 350.0), (3, 0): (-87.5, 350.0), (4, 0): (87.5, 350.0), (5, 0): (175.0, 350.0), (6, 0): (262.5, 350.0), (7, 0): (350.0, 350.0), (0, 1): (-350.0, 262.5), (1, 1): (-262.5, 262.5), (2, 1): (-175.0, 262.5), (3, 1): (-87.5, 262.5), (4, 1): (87.5, 262.5), (5, 1): (175.0, 262.5), (6, 1): (262.5, 262.5), (7, 1): (350.0, 262.5), (0, 2): (-350.0, 175.0), (1, 2): (-262.5, 175.0), (2, 2): (-175.0, 175.0), (3, 2): (-87.5, 175.0), (4, 2): (87.5, 175.0), (5, 2): (175.0, 175.0), (6, 2): (262.5, 175.0), (7, 2): (350.0, 175.0), (0, 3): (-350.0, 87.5), (1, 3): (-262.5, 87.5), (2, 3): (-175.0, 87.5), (3, 3): (-87.5, 87.5), (4, 3): (87.5, 87.5), (5, 3): (175.0, 87.5), (6, 3): (262.5, 87.5), (7, 3): (350.0, 87.5), (0, 4): (-350.0, -87.5), (1, 4): (-262.5, -87.5), (2, 4): (-175.0, -87.5), (3, 4): (-87.5, -87.5), (4, 4): (87.5, -87.5), (5, 4): (175.0, -87.5), (6, 4): (262.5, -87.5), (7, 4): (350.0, -87.5), (0, 5): (-350.0, -175.0), (1, 5): (-262.5, -175.0), (2, 5): (-175.0, -175.0), (3, 5): (-87.5, -175.0), (4, 5): (87.5, -175.0), (5, 5): (175.0, -175.0), (6, 5): (262.5, -175.0), (7, 5): (350.0, -175.0), (0, 6): (-350.0, -262.5), (1, 6): (-262.5, -262.5), (2, 6): (-175.0, -262.5), (3, 6): (-87.5, -262.5), (4, 6): (87.5, -262.5), (5, 6): (175.0, -262.5), (6, 6): (262.5, -262.5), (7, 6): (350.0, -262.5), (0, 7): (-350.0, -350.0), (1, 7): (-262.5, -350.0), (2, 7): (-175.0, -350.0), (3, 7): (-87.5, -350.0), (4, 7): (87.5, -350.0), (5, 7): (175.0, -350.0), (6, 7): (262.5, -350.0), (7, 7): (350.0, -350.0)}

for coord in d:
    f.append(Turtle())
    f[-1].goto(d[coord])
