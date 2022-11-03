
from turtle import *
from os import *




files_path = getcwd()
chdir(files_path)

s = Screen()


startmenu = True


def Startmenu():

    s.delay(0)
    setup( width = 900, height = 800)
    s.bgcolor("black")
    


while True:

    if startmenu:

        Startmenu()

        
