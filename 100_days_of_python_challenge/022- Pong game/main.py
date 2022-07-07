from turtle import Screen, Turtle
from paddle import Paddle
import time

game_is_running = True
turtle = Turtle("square")
turtle.goto(350, 0)

def ff()


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor('gray')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(ff,'Up')
screen.onkey(l_paddle.go_up(), 'w')
screen.onkey(l_paddle.go_down(), 's')
screen.onkey(r_paddle.go_up(), 'Up')
screen.onkey(r_paddle.go_down(), 'Down')

while game_is_running:
    screen.update()


screen.exitonclick()
