from turtle import Turtle, Screen
import turtle
import random


colors = [
    (139, 0, 0),       # Dark Red
    (0, 100, 0),       # Dark Green
    (0, 0, 139),       # Dark Blue
    (47, 79, 79),      # Dark Slate Gray
    (85, 26, 139),     # Dark Purple
    (139, 69, 19),     # Saddle Brown
    (72, 61, 139),     # Dark Slate Blue
    (128, 0, 0),       # Maroon
    (0, 128, 128),     # Teal
    (139, 90, 0),      # Dark Goldenrod
    (112, 128, 144),   # Slate Gray
    (0, 139, 69),      # Spring Green 4
    (105, 105, 105),   # Dim Gray
    (70, 130, 180),    # Steel Blue
    (65, 105, 225),    # Royal Blue
    (34, 139, 34),     # Forest Green
    (139, 134, 78),    # Khaki4
    (119, 136, 153),   # Light Slate Gray
    (139, 71, 93),     # Rosy Brown
    (92, 51, 23),      # Saddle Brown
    (128, 128, 0),     # Olive
    (85, 107, 47),     # Dark Olive Green
    (153, 50, 204),    # Dark Orchid
    (123, 104, 238),   # Medium Slate Blue
    (106, 90, 205),    # Slate Blue
    (72, 61, 139),     # Dark Slate Blue
    (0, 139, 139),     # Dark Cyan
    (139, 0, 139),     # Dark Magenta
    (143, 188, 143),   # Dark Sea Green
    (0, 104, 139)      # Deep Sky Blue 4
]



timmy = Turtle()
turtle.colormode(255)
timmy.pensize(8)
rand_color = random.choice(colors)
print(rand_color)


angles = [0,90,180,270]

# this is going to move randomly chosing the random color for the set forward movements
timmy.speed(0)
for _ in range(200):
    rand_angle = random.choice(angles)
    rand_color = random.choice(colors)
    timmy.color(rand_color)
    timmy.forward(25)
    timmy.right(rand_angle)



screen = Screen()
screen.exitonclick()
# screen.colormode(255)
screen.screensize(600,600)