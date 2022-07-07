from turtle import Turtle

ALIGNMENT = "center"
STYLE = ('Courier', 14, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('cyan')
        self.goto(0, 275)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=STYLE, align=ALIGNMENT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=STYLE, align=ALIGNMENT)
