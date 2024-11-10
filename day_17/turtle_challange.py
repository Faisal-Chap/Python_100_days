import turtle
import random

timmy = turtle.Turtle()
timmy.shape("turtle")

shape_corner = [3,4,5,7,9,11,13,15]
colors = [
    "Red",
    "Green",
    "Blue",
    "Cyan",
    "Magenta",
    "Orange",
    "Purple",
    "Brown",
    "Olive",
    "Slate Gray",
    "Khaki",
    "Sea Green",
    "Violet",
    "Turquoise",
    "Orchid",
 
]


i = 0

def make_shape(shape_angle):
    color = random.choice(colors)
    timmy.color(color)
    for _ in range(shape_corner[i]):
        timmy.forward(100)
        timmy.left(shape_angle)

for corner in shape_corner:
    shape_angle = 360/corner
    make_shape(shape_angle)
    i += 1


screen = turtle.Screen()
screen.exitonclick()