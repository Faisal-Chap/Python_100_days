# import colorgram

# rgb = []
# colors = colorgram.extract(r'day_17\imm.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb.append(new_color)

# print(rgb)


# here is the list of the all colors 
all_colors = [(233, 233, 232), (231, 233, 237), (235, 232, 233), (224, 
233, 227), (207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 206, 107), (132, 177, 203), (158, 46, 
83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 
20, 44), (37, 43, 69), (186, 94, 106), (185, 140, 172), (84, 120, 180), (59, 39, 31), (87, 157, 91), (78, 153, 164), (195, 79, 72), (161, 201, 219), (80, 74, 44), (45, 74, 77), (56, 128, 124), (218, 176, 187), (168, 207, 169), (220, 181, 169)]


import turtle
import random

turtle.colormode(255)
turtle.screensize(1000,1500)
tim = turtle.Turtle()
tim.speed('fast')
tim.penup()


k = 0
y_m = 0
for i in range(10):
    tim.setx(-300)
    for j in range(10):
        tim.sety(-230 - y_m)
        color = random.choice(all_colors)
        tim.dot(20, color)
        tim.forward(65)
    y_m -= 50


screen = turtle.Screen()
screen.exitonclick()
# screen.screensize(200,200)