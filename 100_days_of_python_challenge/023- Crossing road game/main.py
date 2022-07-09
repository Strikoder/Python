import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Cross the road")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.movements()

    # Collusion
    for car in car_manager.all_cars:
        if car.distance(player) < 29:
            game_is_on = False
            scoreboard.game_over()

    # next lvl
    if player.next_level():
        player.go_to_start()
        car_manager.increase_car_speed()
        scoreboard.next_level()

screen.exitonclick()
