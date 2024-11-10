import turtle as t
import random



tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.pensize(1)
# generate random color
def rgb_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# degree = 360
radius = 100
head_move = 3
for i in range(int(360/head_move)): 
    tim.color(rgb_colors())
    tim.circle(radius)
    tim.setheading(head_move)
    head_move += 3





screen = t.Screen()
screen.exitonclick()