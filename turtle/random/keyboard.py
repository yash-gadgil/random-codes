import turtle

s=turtle.getscreen()
s.delay(0)
turtle.title("Triangle Maker")
turtle.ht()

t = turtle.Turtle()
t.penup()
t.speed(0)
t.goto(-500,0)
#t.pendown()


def space():
    t.write(" ", font=("Arial",14,"bold"))
    t.fd(11.25)

def backspace():
    t.undo()
    t.undo()
    t.bk(11.25)

def a():
    t.write("a", font=("Arial",14,"bold"))
    t.fd(10.25)

def b():
    t.write("b", font=("Arial",14,"bold"))
    t.fd(11.25)

def c():
    t.write("c", font=("Arial",14,"bold"))
    t.fd(10.25)

def d():
    t.write("d", font=("Arial",14,"bold"))
    t.fd(11.25)
    
def e():
    t.write("e", font=("Arial",14,"bold"))
    t.fd(10.25)

def f():
    t.write("f", font=("Arial",14,"bold"))
    t.fd(6.5)

def g():
    t.write("g", font=("Arial",14,"bold"))
    t.fd(11.25)

def h():
    t.write("h", font=("Arial",14,"bold"))
    t.fd(10.75)

def i():
    t.write("i", font=("Arial",14,"bold"))
    t.fd(6)

def j():
    t.write("j", font=("Arial",14,"bold"))
    t.fd(6)
    
def k():
    t.write("k", font=("Arial",14,"bold"))
    t.fd(10.25)

def l():
    t.write("l", font=("Arial",14,"bold"))
    t.fd(11.25)

def m():
    t.write("m", font=("Arial",14,"bold"))
    t.fd(11.25)

def n():
    t.write("n", font=("Arial",14,"bold"))
    t.fd(10.25)

def o():
    t.write("o", font=("Arial",14,"bold"))
    t.fd(11.25)

def p():
    t.write("p", font=("Arial",14,"bold"))
    t.fd(11.25)
   
def q():
    t.write("q", font=("Arial",14,"bold"))
    t.fd(10.25)

def r():
    t.write("r", font=("Arial",14,"bold"))
    t.fd(11.25)

def s():
    t.write("s", font=("Arial",14,"bold"))
    t.fd(11.25)

def tw():
    t.write("t", font=("Arial",14,"bold"))
    t.fd(10.25)

def u():
    t.write("u", font=("Arial",14,"bold"))
    t.fd(11.25)

def v():
    t.write("v", font=("Arial",14,"bold"))
    t.fd(11.25)
  
def w():
    t.write("w", font=("Arial",14,"bold"))
    t.fd(10.25)

def x():
    t.write("x", font=("Arial",14,"bold"))
    t.fd(11.25)

def y():
    t.write("y", font=("Arial",14,"bold"))
    t.fd(10.25)

def z():
    t.write("z", font=("Arial",14,"bold"))
    t.fd(11.25)

turtle.listen()

turtle.onkeypress(space," ")
turtle.onkeypress(backspace,"]")

turtle.onkeypress(a,"a")
turtle.onkeypress(b,"b")
turtle.onkeypress(c,"c")
turtle.onkeypress(d,"d")
turtle.onkeypress(e,"e")
turtle.onkeypress(f,"f")
turtle.onkeypress(g,"g")
turtle.onkeypress(h,"h")
turtle.onkeypress(i,"i")
turtle.onkeypress(j,"j")
turtle.onkeypress(k,"k")
turtle.onkeypress(l,"l")
turtle.onkeypress(m,"m")
turtle.onkeypress(n,"n")
turtle.onkeypress(o,"o")
turtle.onkeypress(p,"p")
turtle.onkeypress(q,"q")
turtle.onkeypress(r,"r")
turtle.onkeypress(s,"s")
turtle.onkeypress(tw,"t")
turtle.onkeypress(u,"u")
turtle.onkeypress(v,"v")
turtle.onkeypress(w,"w")
turtle.onkeypress(x,"x")
turtle.onkeypress(y,"y")
turtle.onkeypress(z,"z")

turtle.mainloop()
