from turtle import *
from os import *

chdir("C:\\Users\\Dell\\Desktop\\random codes\\background animation\\yinyang\\@Resources\\yingif")

s = Screen()
s.delay(0)

bg = Turtle()
frames, frames_ = 252, []

for i in range(frames):
    shapename = "frame_"
    
    if i<10:
        shapename += "00" + str(i) + ".gif"
        s.register_shape(shapename)
    elif i<100:
        shapename += "0" + str(i) + ".gif"
        s.register_shape(shapename)
    else:
        shapename += str(i) + ".gif"
        s.register_shape(shapename)
    frames_.append(shapename)

while True:
    for frame in frames_:
        bg.shape(frame)
