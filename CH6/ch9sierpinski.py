import turtle

def drawTriangle(t,p1,p2,p3):
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)

def drawSquare(t,p1,p2,p3,p4):
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.goto(p3)
    t.goto(p4)


def midPoint(p1,p2):
    return ((p1[0]+p2[0])/2.0,(p1[1]+p2[1])/2.0)

def square(myTurtle,p1,p2,p3,p4,depth):
    if depth >0:
        myTurtle.color("green")
        myTurtle.begin_fill()
        square(myTurtle,midPoint(p1,p1),midPoint(p1,p2), midPoint(p1,p3),midPoint(p1,p4), depth-1,)
        myTurtle.end_fill()
        myTurtle.fillcolor("red")
        myTurtle.begin_fill()
        square(myTurtle,midPoint(p2,p1),midPoint(p2,p3), midPoint(p2,p4),midPoint(p2,p2), depth-1,)
        myTurtle.end_fill()
        myTurtle.fillcolor("blue")
        myTurtle.begin_fill()
        square(myTurtle,midPoint(p3,p1),midPoint(p3,p2), midPoint(p3,p3),midPoint(p3,p4), depth-1,)
        myTurtle.end_fill()
        myTurtle.fillcolor("yellow")
        myTurtle.begin_fill()
        square(myTurtle,midPoint(p4,p1),midPoint(p4,p2), midPoint(p4,p3),midPoint(p4,p4), depth-1,)
        myTurtle.end_fill()

    else:
        drawSquare(myTurtle,p1,p2,p3,p4)


def sierpinski(myTurtle,p1,p2,p3,depth):
    if depth > 0:
        myTurtle.color("green")
        myTurtle.begin_fill()
        sierpinski(myTurtle,p1,midPoint(p1,p2),midPoint(p1,p3),depth-1,)
        myTurtle.end_fill()
        
        myTurtle.fillcolor("blue")
        myTurtle.begin_fill()
        sierpinski(myTurtle,p2,midPoint(p2,p3),midPoint(p2,p1),depth-1,)
        myTurtle.end_fill()
        
        myTurtle.fillcolor("red")
        myTurtle.begin_fill()
        sierpinski(myTurtle,p3,midPoint(p3,p1),midPoint(p3,p2),depth-1,)
        myTurtle.end_fill()
        
    else:
        drawTriangle(myTurtle,p1,p2,p3)
        
        
fred = turtle.Turtle()
win = turtle.Screen()

#sierpinski(fred, (-200,-200), (200,-200), (0,200), 3)
square(fred, (-200,-200), (200,-200), (0,200),(-200,0), 4)
win.exitonclick()