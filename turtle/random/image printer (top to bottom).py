from time import perf_counter as clock
from tkinter import filedialog
from PIL import Image
from turtle import *

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("PNG files",
                                                        "*.png*"),
                                                       ("all files",
                                                        "*.*")))
browseFiles()

image = Image.open(filename, "r")

a = clock()

pix_val = list(image.getdata())
width, height = image.size

gt_left = -width/2
gt_top = height/2

s = Screen()
s.delay(0)

t = Turtle()
t.speed(0)
colormode(255) 
t.ht()

t.pu()
t.goto(gt_left,gt_top)
t.pd()

i = 0
h_i = 1

for pixel in pix_val:
    if i == width :
        t.pu()
        t.goto(gt_left, gt_top - h_i)
        t.pd()

        h_i += 1
        i = 0

    rgb_val = pixel[:3]
    
    if (pixel[3] == 0):
        t.pu()
        t.fd(1)
    else:
        t.pd()
        t.pencolor(rgb_val)
        t.fd(1)
    
    i += 1
    
b = clock()

print("time taken: %.2f sec." % (b-a))
