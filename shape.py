import turtle as t
import random

chimmy = t.Turtle()
chimmy.shape("turtle")

colors = ["medium violet red", "royal blue", "green", "purple", "gold", "dark turquoise", "dim gray", "dark orange", "maroon", "pale violet red"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        chimmy.forward(100)
        chimmy.right(angle)

for shape_side_n in range(3, 11):
    chimmy.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()