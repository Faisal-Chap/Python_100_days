import turtle as tt
import random




screen = tt.Screen()
timmy = tt.Turtle()
print(timmy.pos()) 
screen.setup(width= 600, height= 600)
timmy.goto(-screen.window_height() //2, -screen.window_width()//2)
print(timmy.pos())

colors = [ 
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Cyan",
    "Magenta",
    "Orange",
    "Purple",
    "Lime",
    "Pink"
]
j = 0

for i in range(50):
    color = random.choice(colors)
    timmy.color(color)
    timmy.pensize(5)
    if i%2==0:
        timmy.pendown()
        timmy.forward(10)
    else:
        timmy.penup()
        timmy.forward(10)





screen.exitonclick()
# screen.
# screen.setup (width=200, height=200, startx=0, starty=0)
