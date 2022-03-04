#####Turtle Intro######

import turtle as t
import random

screen = t.Screen()

tim = t.Turtle()
tim.speed("fastest")

t.colormode = (255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        screen.colormode(255)
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + size_of_gap)


draw(2)

screen.exitonclick()
