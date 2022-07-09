import turtle
from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.lvl = 1
        self.penup()
        self.goto(-283, 279)
        self.color("pink")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"lvl: {self.lvl}", align="left", font=FONT)

    def next_level(self):
        self.lvl += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("blue")
        self.write(f"GAME OVER", align="center", font=FONT)
