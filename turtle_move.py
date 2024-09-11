import turtle


def upmove():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def downmove():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def leftmove():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def rightmove():
    turtle.setheading(360)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(upmove,'w')
turtle.onkey(leftmove,'a')
turtle.onkey(downmove,'s')
turtle.onkey(rightmove,'d')
turtle.onkey(restart,'Escape')
turtle.listen()

turtle.exitonclick()

