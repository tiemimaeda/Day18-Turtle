import turtle as t
import random

chimmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


chimmy.shape("turtle")
chimmy.pensize(15)
chimmy.speed("fastest")

# colors = ["medium violet red", "royal blue", "green", "purple", "gold", "dark turquoise", "dim gray", "dark orange", "maroon", "pale violet red"]
diretions = [0, 90, 180, 270]

for _ in range(200):
    chimmy.color(random_color())
    chimmy.forward(30)
    chimmy.setheading(random.choice(diretions))

screen = t.Screen()
screen.exitonclick()