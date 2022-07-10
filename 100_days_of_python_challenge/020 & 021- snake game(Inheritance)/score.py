from turtle import Turtle

ALIGNMENT = "center"
STYLE = ('Courier', 14, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color('cyan')
        self.goto(0, 275)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest score: {self.high_score}", font=STYLE, align=ALIGNMENT)
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"GAME OVER", font=STYLE, align=ALIGNMENT)
