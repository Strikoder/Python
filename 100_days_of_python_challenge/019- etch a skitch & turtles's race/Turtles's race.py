import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1080, height=720)
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
ninja_turtles = []
race_finished = True


user_bet = screen.textinput(title="Make your bet, please!", prompt="Which turtle gonna win the race? Enter a color: ")


for turtle_loc in range(len(colors)):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_loc])
    new_turtle.goto(x=-480, y=-30 * turtle_loc)
    ninja_turtles.append(new_turtle)

if user_bet:
    race_finished = False

while not race_finished:
    for ninja_turtle in ninja_turtles:
        if ninja_turtle.xcor() > 480:
            race_finished = True
            if ninja_turtle.pencolor() == user_bet:
                print("You have won, congratz!")
            else:
                print("You have lost(")

        speed = random.randint(10, 20)
        ninja_turtle.forward(speed)


screen.exitonclick()
