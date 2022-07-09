from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.forward(MOVE_DISTANCE * -1)

    def move_left(self):
        self.left(90)
        self.forward(MOVE_DISTANCE)
        self.right(90)

    def move_right(self):
        self.right(90)
        self.forward(MOVE_DISTANCE)
        self.left(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def next_level(self):
        return self.ycor() >= FINISH_LINE_Y