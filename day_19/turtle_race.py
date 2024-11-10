import turtle
import random

game_on = False
screen = turtle.Screen()
screen.setup(width=700,height=600)

user_bet = screen.textinput(title="Wellcome to the Turtle Race !!!",prompt="Which Turtle you would chose?  ")
if user_bet:
    game_on = True
colors = [ 
    "Red",
    "Green",
    "Blue",
    "Cyan",
    "Magenta",
    "Orange",
    "Purple"
]
# turtle.setup(width=700,height=600)
y_incr = 0
objs=[]
for i in range(6):
    obj = 'timmy' +str(i)
    color = colors[i]
    obj = turtle.Turtle() 
    obj.speed("fastest")
    obj.shape('turtle')
    obj.penup()
    obj.color(color)
    obj.setx(-300)
    obj.sety(-100 + y_incr)
    y_incr += 50
    objs.append(obj)



def limit():
    limit = []
    for i in range(-300,300):
        limit.append(i)
    return limit

limit_list = limit()

def race_start():
    global game_on
    speed_list = [5,10,15,25,30,50]
    while game_on:
        for i in range(6):
            c_obj = objs[i]
            rand_speed = random.choice(speed_list)
            c_obj.forward(rand_speed)
            c_x = int(c_obj.xcor())

            if c_x >= 270:
                game_on = False 
                # print(c_x) 
                return c_obj.pencolor()
        
w_color = race_start()
if user_bet == w_color:
    print('You won')
else:
    print('You lose')




# screen.onclick('s',race_start)
# screen.listen()
# screen.exitonclick()