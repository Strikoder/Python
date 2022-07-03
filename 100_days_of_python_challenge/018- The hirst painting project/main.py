"""#####Turtle Intro######
import turtle
import random

directions = [0, 90, 180, 270]


def draw_a_square():
    for i in range(4):
        t.forward(100)
        t.right(90)


def draw_dashed_line():
    for i in range(100):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


def draw_shapes():
    """"""for i in range(3,9):
        j=i+1
        for j in range(4,9):
            t.forward(60)
            t.right(360/j)""""""
            
    for i in range(3, 11):
        for j in range(i):
            t.forward(60)
            t.right(360 / i)
            t.forward(60)


def random_walk():
    t.speed(10)
    t.width(16)
    for i in range(100):
        t.setheading(random.choice(directions))
        t.forward(60)
        t.color(random_color())


def draw_spirograph(size_between_circules):
    for _ in range(int(360/size_between_circules)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading()+size_between_circules)


t = turtle.Turtle()
turtle.colormode(255)
t.shape("turtle")
t.color("blue")
t.setheading(0)

t.speed("fastest")
draw_spirograph(5)
input()
"""

import turtle as turtle_module
import random
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


turtle_module.colormode(255)
ninja_turtle = turtle_module.Turtle()
ninja_turtle.speed(20)
ninja_turtle.penup()
ninja_turtle.hideturtle()

ninja_turtle.setheading(225)
ninja_turtle.forward(300)
ninja_turtle.setheading(0)

number_of_dots = 80

for dot_count in range(1, number_of_dots + 1):
    ninja_turtle.dot(20, random.choice(color_list))
    ninja_turtle.forward(50)

    if dot_count % 10 == 0:
        ninja_turtle.setheading(90)
        ninja_turtle.forward(50)
        ninja_turtle.setheading(180)
        ninja_turtle.forward(500)
        ninja_turtle.setheading(0)

