import numpy as np  
import turtle as t   


win = t.getscreen()
win.setup(600,600)
win.bgcolor("black")
win.title("Pentab")
win.listen()
pen = t.Turtle()
pen.color("white")
pen.speed(0)
t.ht()


"""
Use (CTRL + ]) to indent rightward and (CTRL + [) to indent leftward
"""
def pentab():                                    
    def pencil(x,y):
        pen.ondrag(None)
        pen.seth(pen.towards(x,y))
        pen.goto(x,y)
        pen.ondrag(pencil)
           
    def move(x,y):
        pen.up()
        pen.goto(x,y)
        pen.down()
        
    def eraser():
        for i in range(10):
            pen.undo()
    
    def pencolor():
        colors=np.array(["red","blue","lime","white","maroon","cyan","fuchsia","gold"])
        color = np.random.choice(colors)
        pen.color(color)
        
    def star():
        for i in range(5):
            pen.fd(100)
            pen.lt(144)
            
    def triangle():
        for i in range(3):
            pen.fd(100)
            pen.lt(120)
    
    def square():
        for i in range(4):
            pen.fd(100)
            pen.lt(90)
    
    def pentagon():
        for i in range(5):
            pen.fd(100)
            pen.lt(72)
    
    def hexagon():
        for i in range(6):
            pen.fd(100)
            pen.lt(60)
            
    def invoke():
        pen.ondrag(pencil)
        win.onclick(move,btn=1)
        win.onclick(lambda x,y: pen.clear(),btn=3)
        win.listen()
        win.onkey(eraser,key="Left")
        win.onkey(pencolor,key="@")
        win.onkey(lambda: pen.circle(75),"c")
        win.onkey(lambda: pen.fd(100),"l")
        win.onkey(lambda: pen.dot(10),"d")
        win.onkey(star,key="*")
        win.onkey(triangle,key="t")
        win.onkey(square,key="s")
        win.onkey(pentagon,key="p")
        win.onkey(hexagon,key="h")
    invoke()
   
    
pentab()      
t.mainloop()    