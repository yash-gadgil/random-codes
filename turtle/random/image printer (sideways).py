from time import perf_counter as clock
from PIL import Image
from turtle import *
from os import *

chdir("C:\\Users\\Dell\\Downloads")

image = Image.open("flappyup.png", "r")

a = clock()

pix_val = list(image.getdata())
width, height = image.size

gt_left = -width/2
gt_top = height/2

s = Screen()
s.delay(0)

colormode(255) 

turtles = [Turtle() for _ in range(height)]

t = 2
i = 0

for turtle in turtles:
    turtle.pu()
    turtle.speed(0)
    turtle.ht()

    if t == 1:
        turtle.goto(gt_left, gt_top)
    else:
        turtle.goto(gt_left, gt_top - t)
    
    turtle.pd()
    
    t += 1
    i += 1

pix_rows = []

for width_cut in range(height):
    pix_rows.append(pix_val[width * (width_cut) : width * (width_cut + 1)])

for pixel in range(width):
    
    row = 0
    
    for turtle in turtles:
        
        rgb_val = pix_rows[row][pixel][:3]

        if (pix_rows[row][pixel][3] == 0):
            turtle.pu()
            turtle.fd(1)
        else:
            turtle.pd()
            turtle.pencolor(rgb_val)
            turtle.fd(1)

        row += 1

b = clock()

print("time taken: %.2f sec." % (b-a))


