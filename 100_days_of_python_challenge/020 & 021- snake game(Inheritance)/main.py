from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaky snake game")
screen.tracer(0)
screen.bgcolor('gray')


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()
