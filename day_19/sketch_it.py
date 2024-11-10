import turtle


tim = turtle.Turtle()


def f():
    tim.forward(20)
def b():
    tim.setheading(180)
    tim.forward(20)
def u():
    tim.setheading(90)
    tim.forward(20)
def d():
    tim.setheading(270)
    tim.forward(20)
def tilt_clk():
    tim.right(9)
def tilt_aclk():
    tim.left(9)
def clear():
    tim.clear()


screen = turtle.Screen()
screen.onkey(key='d',fun=tilt_clk)
screen.onkey(key='a',fun=tilt_aclk)

screen.onkey(key="Up",fun=u)
screen.onkey(key="Down",fun=d)
screen.onkey(key="Left",fun=b)
screen.onkey(key="Right",fun=f)

screen.onkey(key='c',fun=clear)
screen.listen()
screen.exitonclick()