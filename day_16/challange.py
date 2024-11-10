# this code is written in response to the challange by the turtle Module

from turtle import Turtle, Screen




timmy = Turtle()
timmy.color("red")
timmy.shape("turtle")
for i in range(0, 10):

    timmy.forward(i)
    timmy.left(90)
    timmy.forward(i)
    timmy.right(90)
    print(timmy.position())



box = Screen()
box.exitonclick() 
