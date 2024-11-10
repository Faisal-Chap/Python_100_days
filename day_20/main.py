import turtle
import time
from snake import Snake

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
turtle.colormode(255)
screen.tracer(0)

# Game state
is_game_on = True

# Create the Snake object
snake = Snake()

# Main game loop
while is_game_on:
    screen.update()
    snake.move()
    time.sleep(0.2)

screen.mainloop()
