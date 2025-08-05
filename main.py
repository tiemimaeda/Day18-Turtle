import turtle as turtle_module
import random

turtle_module.colormode(255)
chimmy = turtle_module.Turtle()
chimmy.speed("fastest")
chimmy.penup()
chimmy.hideturtle()

color_list = [(159, 98, 27), (232, 240, 235), (44, 106, 148), (18, 35, 56), (236, 120, 40), (237, 80, 95), (221, 212, 2), (132, 215, 207),
              (237, 96, 38), (149, 183, 217), (210, 154, 162), (52, 91, 86), (164, 46, 135), (86, 181, 7), (134, 217, 220), (234, 210, 56), (214, 130, 25)]

chimmy.setheading(225)
chimmy.forward(300)
chimmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    chimmy.dot(20, random.choice(color_list))
    chimmy.forward(50)

    if dot_count % 10 == 0:
        chimmy.setheading(90)
        chimmy.forward(50)
        chimmy.setheading(180)
        chimmy.forward(500)
        chimmy.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()