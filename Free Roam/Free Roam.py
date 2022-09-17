
import turtle
import os
#import random

os.chdir(os.getcwd())

d_alive = True
d1_alive = True

f_alive = True
falling = True

'''
t = 0
u1 = 44.27188724235731
u = 0
v = 0
'''

s=turtle.getscreen()
s.delay(0)
turtle.title("Free Roam")
turtle.bgcolor("green")
turtle.ht()

s.register_shape("tree1.gif")
s.register_shape("player1right1.gif")
s.register_shape("player1left1.gif")
s.register_shape("player1left1inv.gif")
s.register_shape("player1right1inv.gif")
s.register_shape("portal1.gif")
s.register_shape("chaser1.gif")
s.register_shape("crab1.gif")
s.register_shape("gundude1.gif") 
s.register_shape("player2left.gif") 
s.register_shape("bulletright.gif")
s.register_shape("bulletleft.gif")
s.register_shape("player2right.gif")
'''
s.register_shape("flappyup.gif")
s.register_shape("flappydown.gif") 
s.register_shape("birddude1.gif")
s.register_shape("background1.gif")
s.register_shape("pipe30top.gif")
s.register_shape("pipe30bottom.gif")
s.register_shape("pipe20top.gif")
s.register_shape("pipe40bottom.gif")
s.register_shape("pipe40top.gif")
s.register_shape("pipe20bottom.gif")
s.register_shape("pipe15top.gif")
s.register_shape("pipe45bottom.gif")
s.register_shape("pipe15bottom.gif")
s.register_shape("pipe45top.gif")
'''

x=0
y=0
playerface = True
inverted = False

chest = turtle.Turtle()
chest.shape("square")
chest.color("red")
chest.speed(0)
chest.penup()
chest.goto(x-350,y-350)

portal = turtle.Turtle()
portal.shape("portal1.gif")
portal.speed(0)
portal.penup()
portal.goto(-950,950)

portal1 = portal.clone()
portal1.penup()
portal1.goto(950,950)

player = turtle.Turtle()
player.shape("player1right1.gif")

crab = turtle.Turtle()
crab.shape("crab1.gif")
crab.speed(0)
crab.penup()
crab.goto(-650,0)

tree1 = turtle.Turtle()
tree1.shape("tree1.gif")
tree1.speed(0)
tree1.penup()
tree1.goto(x-350,y-150)

tree2 = tree1.clone()
tree2.penup()
tree2.goto(x+150,y+350)

tree3 = tree1.clone()
tree3.penup()
tree3.goto(350,-450)

tree4 = tree1.clone()
tree4.penup()
tree4.goto(-350,-550)

tree5 = tree1.clone()
tree5.penup()
tree5.goto(550,150)

gundude = turtle.Turtle()
gundude.shape("gundude1.gif")
gundude.speed(0)
gundude.penup()
gundude.goto(650,50)

tplayer = turtle.Turtle()
tplayer.shape("player1right1.gif")
tplayer.speed(0)
tplayer.penup()
tplayer.ht()

enemy = turtle.Turtle()
enemy.shape("chaser1.gif")
enemy.speed(0)
enemy.penup()
enemy.ht()

dummy = turtle.Turtle()
dummy.shape("player2left.gif")
dummy.speed(0)
dummy.penup()
dummy.ht()

bullet = turtle.Turtle()
bullet.shape("bulletright.gif")
bullet.speed(0)
bullet.penup()
bullet.ht()

dummy1 = dummy.clone()
dummy1.shape("player2right.gif")
dummy1.ht()
dummy1.penup()
'''
birddude = turtle.Turtle()
birddude.shape("birddude1.gif")
birddude.speed(0)
birddude.penup()
birddude.goto(50,-550)

fbackground = turtle.Turtle()
fbackground.shape("background1.gif")
fbackground.speed(0)
fbackground.penup()
fbackground.ht()

flappy = turtle.Turtle()
flappy.shape("flappyup.gif")
flappy.speed(0)
flappy.penup()
flappy.ht()

pipe30top = turtle.Turtle()
pipe30top.shape("pipe30top.gif")
pipe30top.speed(0)
pipe30top.penup()
pipe30top.ht()

pipe30bottom = turtle.Turtle()
pipe30bottom.shape("pipe30bottom.gif")
pipe30bottom.speed(0)
pipe30bottom.penup()
pipe30bottom.ht()

pipe40bottom = turtle.Turtle()
pipe40bottom.shape("pipe40bottom.gif")
pipe40bottom.speed(0)
pipe40bottom.penup()
pipe40bottom.ht()

pipe20top = turtle.Turtle()
pipe20top.shape("pipe20top.gif")
pipe20top.speed(0)
pipe20top.penup()
pipe20top.ht()

pipe40top = turtle.Turtle()
pipe40top.shape("pipe40top.gif")
pipe40top.speed(0)
pipe40top.penup()
pipe40top.ht()

pipe20bottom = turtle.Turtle()
pipe20bottom.shape("pipe20bottom.gif")
pipe20bottom.speed(0)
pipe20bottom.penup()
pipe20bottom.ht()

pipe15top = turtle.Turtle()
pipe15top.shape("pipe15top.gif")
pipe15top.speed(0)
pipe15top.penup()
pipe15top.ht()

pipe45bottom = turtle.Turtle()
pipe45bottom.shape("pipe45bottom.gif")
pipe45bottom.speed(0)
pipe45bottom.penup()
pipe45bottom.ht()

pipe15bottom = turtle.Turtle()
pipe15bottom.shape("pipe15bottom.gif")
pipe15bottom.speed(0)
pipe15bottom.penup()
pipe15bottom.ht()

pipe45top = turtle.Turtle()
pipe45top.shape("pipe45top.gif")
pipe45top.speed(0)
pipe45top.penup()
pipe45top.ht()

'''
'''
bullet1 = bullet.clone()
bullet1.penup()
bullet1.ht()

bullet2 = bullet.clone()
bullet2.penup()
bullet2.ht()

bullet3 = bullet.clone()
bullet3.penup()
bullet3.ht()
'''



def playerUp():
    chest.sety(chest.ycor()-25)
    portal.sety(portal.ycor()-25)
    portal1.sety(portal1.ycor()-25)
    tree1.sety(tree1.ycor()-25)
    tree2.sety(tree2.ycor()-25)
    tree3.sety(tree3.ycor()-25)
    tree4.sety(tree4.ycor()-25)
    tree5.sety(tree5.ycor()-25)
    crab.sety(crab.ycor()-25)
    gundude.sety(gundude.ycor()-25)
    #birddude.sety(birddude.ycor()-25)

def playerDown():
    chest.sety(chest.ycor()+25)
    portal.sety(portal.ycor()+25)
    portal1.sety(portal1.ycor()+25)
    tree1.sety(tree1.ycor()+25)
    tree2.sety(tree2.ycor()+25)
    tree3.sety(tree3.ycor()+25)
    tree4.sety(tree4.ycor()+25)
    tree5.sety(tree5.ycor()+25)
    crab.sety(crab.ycor()+25)
    gundude.sety(gundude.ycor()+25)
    #birddude.sety(birddude.ycor()+25)

def playerRight():
    if inverted == True:
        player.shape("player1right1inv.gif")
    else:
        player.shape("player1right1.gif")
    chest.setx(chest.xcor()-25)
    portal.setx(portal.xcor()-25)
    portal1.setx(portal1.xcor()-25)
    tree1.setx(tree1.xcor()-25)
    tree2.setx(tree2.xcor()-25)
    tree3.setx(tree3.xcor()-25)
    tree4.setx(tree4.xcor()-25)
    tree5.setx(tree5.xcor()-25)
    crab.setx(crab.xcor()-25)
    gundude.setx(gundude.xcor()-25)
    #birddude.setx(birddude.xcor()-25)
    global playerface
    playerface = True

def playerLeft():
    if inverted == True:
        player.shape("player1left1inv.gif")
    else:
        player.shape("player1left1.gif")
    chest.setx(chest.xcor()+25)
    portal.setx(portal.xcor()+25)
    portal1.setx(portal1.xcor()+25)
    tree1.setx(tree1.xcor()+25)
    tree2.setx(tree2.xcor()+25)
    tree3.setx(tree3.xcor()+25)
    tree4.setx(tree4.xcor()+25)
    tree5.setx(tree5.xcor()+25)
    crab.setx(crab.xcor()+25)
    gundude.setx(gundude.xcor()+25)
    #birddude.setx(birddude.xcor()+25)
    global playerface
    playerface=False
'''
def player2Up():
    if 500>player2.ycor():
        player2.sety(player2.ycor()+50)
        if shooting:
            bullet1.sety(bullet1.ycor()+50)

def player2Down():
    if -500<player2.ycor():
        player2.sety(player2.ycor()-50)
        if shooting:
            bullet1.sety(bullet1.ycor()-50)

player2facing = False

def player2Right():
    if player2.xcor()<950:
        player2.setx(player2.xcor()+50)
        player2.shape("player2right.gif")
        global player2facing
        player2facing = True
        if shooting:
            bullet1.setx(bullet1.xcor()+50)

def player2Left():
    if -950<player2.xcor():
        player2.setx(player2.xcor()-50)
        player2.shape("player2left.gif")
        global player2facing
        player2facing = False
        if shooting:
            bullet1.setx(bullet1.xcor()-50)

def player2Shoot():
    if bullet1.pos() == player2.pos():
        bullet1.st()
        if player2facing:
            for i in range(200):
                bullet1.setx(bullet1.xcor()+10)
        else:
            for i in range(200):
                bullet1.setx(bullet1.xcor()-10)

'''

shot = False

def playertUp():
    if 500>tplayer.ycor():
        tplayer.sety(tplayer.ycor()+50)
        if shooting:
            if not shot:
                bullet.sety(bullet.ycor()+50)
            #bullet1.sety(bullet1.ycor()+50)
            #bullet2.sety(bullet2.ycor()+50)
            #bullet3.sety(bullet3.ycor()+50)
           
tplayerfacing = True

def playertDown():
    if -500<tplayer.ycor():
        tplayer.sety(tplayer.ycor()-50)
        if shooting:
            if not shot:
                bullet.sety(bullet.ycor()-50)
            #bullet1.sety(bullet1.ycor()-50)
            #bullet2.sety(bullet2.ycor()-50)
            #bullet3.sety(bullet3.ycor()-50)

def playertRight():
    if tplayer.xcor()<950:
        tplayer.shape("player1right1.gif")
        global tplayerfacing
        tplayerfacing = True
        if not shooting:
            tplayer.setx(tplayer.xcor()+50)
        elif shooting:
            if tplayer.xcor()<300:
                tplayer.setx(tplayer.xcor()+50)
                if not shot:
                    bullet.setx(bullet.xcor()+50)
            #bullet1.setx(bullet1.xcor()+50)
            #bullet2.setx(bullet2.xcor()+50)
            #bullet3.setx(bullet3.xcor()+50)

def playertLeft():
    if -950<tplayer.xcor():
        tplayer.shape("player1left1.gif")
        global tplayerfacing
        tplayerfacing = False
        if not shooting:
            tplayer.setx(tplayer.xcor()-50)
        elif shooting:
            if -300<tplayer.xcor():
                tplayer.setx(tplayer.xcor()-50)
                if not shot:
                    bullet.setx(bullet.xcor()-50)
            #bullet1.setx(bullet1.xcor()-50)
            #bullet2.setx(bullet2.xcor()-50)
            #bullet3.setx(bullet3.xcor()-50)



def playertShoot():
    if bullet.pos() == tplayer.pos():
        bullet.st()
        global shot
        global d_alive
        global d1_alive
        shot = True
        #global bulletxcor
        #global bulletycor
        if tplayerfacing:
            for l in range(100):
                bullet.shape("bulletright.gif")
                bullet.setx(bullet.xcor()+10)
                #bulletxcor = bullet.xcor()
                if 600<bullet.xcor()<620 and bullet.ycor() == 0:
                    dummy.ht()
                    bullet.ht()
                    d_alive = False
                    break
        else:
            for i in range(100):
                bullet.shape("bulletleft.gif")
                bullet.setx(bullet.xcor()-10)
                #bulletxcor = bullet.xcor()
                if -600>bullet.xcor()>-620 and bullet.ycor() == 150:
                    dummy1.ht()
                    bullet.ht()
                    d1_alive = False
                    #shooting = d_alive or d1_alive
                    break
        bullet.ht()

def playertReload():
    global shot
    shot = False
    bullet.goto(tplayer.xcor(),tplayer.ycor())

tag = False
alive = True
shooting = False
    
'''
def Flap():
    global falling
    falling = False
    global t
    t = 0
    u1 = 44.27188724235731
    flappy.shape("flappydown.gif")
    for i in range(2):
        v1 = u1 - 9.8*t
        flappy.bk(v1)
        t+=1
    t = 0
    global u
    u = 0
    global v
    v = 0
    falling = True
    flappy.shape("flappyup.gif")
    s.update()
'''

#minigames
def playerInteract():
    if 50>crab.xcor()>-50 and 50>crab.ycor()>-50:
        global tag
        if not tag:
            s.delay(10)
            turtle.bgcolor("#00FFFF")
            
            tplayer.goto(0,0)
            enemy.goto(0,500)
            
            tplayer.st()
            enemy.st()
            player.ht()
            chest.ht()
            portal.ht()
            portal1.ht()
            tree1.ht()
            tree2.ht()
            tree3.ht()
            tree4.ht()
            tree5.ht()
            crab.ht()
            gundude.ht()
            #birddude.ht()
            
            tag = True
            
            turtle.listen()
            turtle.onkeypress(playertUp,"Up")
            turtle.onkeypress(playertDown,"Down")
            turtle.onkeypress(playertRight,"Right")
            turtle.onkeypress(playertLeft,"Left")
            
            global alive
            alive=True
            
            while alive:
                enemy.setheading(enemy.towards(tplayer.pos()))
                enemy.fd(10)
                if 0<enemy.distance(tplayer)<5:
                    alive=False
                    
                    
                s.update()
            if not alive:
                s.delay(0)
                turtle.bgcolor("green")
                tplayer.ht()
                enemy.ht()
                player.st()
                chest.st()
                portal.st()
                portal1.st()
                tree1.st()
                tree2.st()
                tree3.st()
                tree4.st()
                tree5.st()
                crab.st()
                gundude.st()
                #birddude.st()
                tag = False
    
    
    
    if 50>gundude.xcor()>-50 and 50>gundude.ycor()>-50:
        global d_alive
        global d1_alive
        d_alive = True
        d1_alive = True
        global shooting
        if not shooting:
            s.delay(5)
            shooting = True
            #d_alive = True
            #d1_alive = True
            turtle.bgcolor("gray")
            
            tplayer.goto(0,0)
            bullet.goto(0,0)
            dummy.goto(600,0)
            dummy1.goto(-600,150)
            
            tplayer.st()
            dummy.st()
            dummy1.st()
            player.ht()
            chest.ht()
            portal.ht()
            portal1.ht()
            tree1.ht()
            tree2.ht()
            tree3.ht()
            tree4.ht()
            tree5.ht()
            crab.ht()
            gundude.ht()
            #birddude.ht()
            
            
            turtle.listen()
            turtle.onkeypress(playertUp,"Up")
            turtle.onkeypress(playertDown,"Down")
            turtle.onkeypress(playertRight,"Right")
            turtle.onkeypress(playertLeft,"Left")
            turtle.onkeypress(playertShoot,"0")
            turtle.onkeypress(playertReload,"1")
            
            '''
            turtle.onkeypress(player2Up,"t")
            turtle.onkeypress(player2Down,"g")
            turtle.onkeypress(player2Right,"h")
            turtle.onkeypress(player2Left,"f")
            turtle.onkeypress(player2Shoot," ")
            '''
            
            while shooting:
                
                shooting = d_alive or d1_alive
                
                '''
                #print(bullet.pos())
                global bulletxcor
                global bulletycor
                
                print(bullet.xcor())
                
                if 600<bullet.xcor()<1001  and bullet.ycor() == 0:
                    shooting = False
                '''
                
                s.update()
            
            if not shooting:
                s.delay(0)
                turtle.bgcolor("green")
                tplayer.ht()
                dummy.ht()
                dummy1.ht()
                player.st()
                chest.st()
                portal.st()
                portal1.st()
                tree1.st()
                tree2.st()
                tree3.st()
                tree4.st()
                tree5.st()
                crab.st()
                gundude.st()
                #birddude.st()
                #d_alive = True
                #d1_alive = True
    '''
    if 50>birddude.xcor()>-50 and 50>birddude.ycor()>-50:
        
        f_alive = True
        global falling
        falling = True
        
        fbackground.st()
        flappy.st()
        pipe30top.st()
        pipe30top.st()
        pipe30bottom.st()
        pipe40bottom.st()
        pipe20top.st()
        pipe40top.st()
        pipe20bottom.st()
        pipe15top.st()
        pipe45bottom.st()
        pipe15bottom.st()
        pipe45top.st()
        player.ht()
        chest.ht()
        portal.ht()
        portal1.ht()
        tree1.ht()
        tree2.ht()
        tree3.ht()
        tree4.ht()
        tree5.ht()
        crab.ht()
        gundude.ht()
        birddude.ht()
        
        flappy.goto(-750,0)
        flappy.rt(90)
        
        pipe30top.goto(0,300)
        pipe30bottom.goto(0,-300)
        pipe20top.goto(400,370)
        pipe40bottom.goto(400,-250)
        pipe40top.goto(800,250)
        pipe20bottom.goto(800,-370)
        pipe15top.goto(1200,470)
        pipe45bottom.goto(1200,-150)
        pipe15bottom.goto(1650,-470)
        pipe45top.goto(1650,150)

        def Flap():
            global falling
            falling = False
            global t
            t = 0
            if not falling:
                u = 0
                v = 0
            u1 = 44.27188724235731
            flappy.shape("flappydown.gif")
            for i in range(2):
                v1 = u1 - 9.8*t
                flappy.bk(v1)
                t+=1
            t = 0
'''
'''
            global u
            u = 0
            global v
            v = 0
'''
'''
            falling = True
            flappy.shape("flappyup.gif")
            s.update()
        
        turtle.listen()
        turtle.onkeypress(Flap,"f")
        
        t = 0
        u = 0

        while f_alive:
            
            pipe30top.setx(pipe30top.xcor()-10)
            pipe30bottom.setx(pipe30bottom.xcor()-10)
            pipe20top.setx(pipe20top.xcor()-10)
            pipe40bottom.setx(pipe40bottom.xcor()-10)
            pipe40top.setx(pipe40top.xcor()-10)
            pipe20bottom.setx(pipe20bottom.xcor()-10)
            pipe15top.setx(pipe15top.xcor()-10)
            pipe45bottom.setx(pipe45bottom.xcor()-10)
            pipe45top.setx(pipe45top.xcor()-10)
            pipe15bottom.setx(pipe15bottom.xcor()-10)
            
            t+=0.025
            if falling:
                v = u + 10*t
                #flappy.sety(flappy.ycor()-v)
                flappy.fd(v)
                u = v
                
            print(v)
            
            if pipe30top.xcor()<-1100:
                pipe30top.ht()
                pipe30bottom.ht()
                pipe30top.setx(pipe30top.xcor()+2100)
                pipe30bottom.setx(pipe30bottom.xcor()+2100)
                pipe30bottom.st()
                pipe30top.st()
                
            if pipe20top.xcor()<-1100:
                pipe20top.ht()
                pipe40bottom.ht()
                pipe20top.setx(pipe20top.xcor()+2100)
                pipe40bottom.setx(pipe40bottom.xcor()+2100)
                pipe40bottom.st()
                pipe20top.st()
            
            if pipe40top.xcor()<-1100:
                pipe40top.ht()
                pipe20bottom.ht()
                pipe40top.setx(pipe40top.xcor()+2100)
                pipe20bottom.setx(pipe20bottom.xcor()+2100)
                pipe20bottom.st()
                pipe40top.st()
            
            if pipe15top.xcor()<-1100:
                pipe15top.ht()
                pipe45bottom.ht()
                pipe15top.setx(pipe15top.xcor()+2100)
                pipe45bottom.setx(pipe45bottom.xcor()+2100)
                pipe45bottom.st()
                pipe15top.st()
            
            if pipe45top.xcor()<-1100:
                pipe45top.ht()
                pipe15bottom.ht()
                pipe45top.setx(pipe45top.xcor()+2100)
                pipe15bottom.setx(pipe15bottom.xcor()+2100)
                pipe15bottom.st()
                pipe45top.st()
              
            
            if -630>pipe30top.xcor()>-870 and (flappy.ycor()<-70 or flappy.ycor()>69):
                f_alive = False
            
            if -630>pipe20top.xcor()>-870 and (flappy.ycor()<69 or flappy.ycor()>215):
                f_alive = False
            
            if -630>pipe40top.xcor()>-870 and (flappy.ycor()<-210 or flappy.ycor()>-65):
                f_alive = False
            
            if -630>pipe15top.xcor()>-870 and (flappy.ycor()<100 or flappy.ycor()>350):
                f_alive = False
                
            if -630>pipe45top.xcor()>-870 and (flappy.ycor()>-100 or flappy.ycor()<-350):
                f_alive = False
            
            if flappy.ycor()<-500 or flappy.ycor()>500:
                f_alive = False
            
            s.update()
        
        
        
            
            if not f_alive:
                flappy.ht()
                fbackground.ht()
                pipe30top.ht()
                pipe30bottom.ht()
                pipe40bottom.ht()
                pipe20top.ht()
                pipe40top.ht()
                pipe20bottom.ht()
                pipe15top.ht()
                pipe45bottom.ht()
                pipe15bottom.ht()
                pipe45top.ht()
                player.st()
                chest.st()
                portal.st()
                portal1.st()
                tree1.st()
                tree2.st()
                tree3.st()
                tree4.st()
                tree5.st()
                crab.st()
                gundude.st()
                birddude.st()
            
'''
            
            
    

def playerinv():
    global inverted
    if inverted == False:
        if playerface==True:
            player.shape("player1right1inv.gif")
        elif playerface==False:
            player.shape("player1left1inv.gif")
    else:
        if playerface==True:
            player.shape("player1right1.gif")
        elif playerface==False:
            player.shape("player1left1.gif")
    inverted = not inverted

def teleport():
    chest.setx(chest.xcor()-1900)
    portal.setx(portal.xcor()-1900)
    portal1.setx(portal1.xcor()-1900)
    tree1.setx(tree1.xcor()-1900)
    tree2.setx(tree2.xcor()-1900)
    tree3.setx(tree3.xcor()-1900)
    tree4.setx(tree4.xcor()-1900)
    tree5.setx(tree5.xcor()-1900)
    crab.setx(crab.xcor()-1900)
    gundude.setx(gundude.xcor()-1900)
    #birddude.setx(birddude.xcor()-1900)
    
def teleport1():
    chest.setx(chest.xcor()+1900)
    portal.setx(portal.xcor()+1900)
    portal1.setx(portal1.xcor()+1900)
    tree1.setx(tree1.xcor()+1900)
    tree2.setx(tree2.xcor()+1900)
    tree3.setx(tree3.xcor()+1900)
    tree4.setx(tree4.xcor()+1900)
    tree5.setx(tree5.xcor()+1900)
    crab.setx(crab.xcor()+1900)
    gundude.setx(gundude.xcor()+1900)
    #birddude.setx(birddude.xcor()+1900)
    
turtle.listen()
turtle.onkeypress(playerUp,"w")
turtle.onkeypress(playerDown,"s")
turtle.onkeypress(playerRight,"d")
turtle.onkeypress(playerLeft,"a")
turtle.onkeypress(playerinv,"r")
turtle.onkeypress(playerInteract,"e")
#turtle.onkeypress(playerShoot,"y")


while True:
    if chest.pos()==player.pos():
        player.ht()
    else:
        player.st()
    
    if inverted == False:
        if -50<portal.xcor()<50 and -50<portal.ycor()<50:
            teleport()
    elif inverted == True:
        if -50<portal1.xcor()<50 and -50<portal1.ycor()<50:
            teleport1()
    s.update()

