from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []  # type: turtle.Turtle
        self.__draw_body()
        self.head = self.segments[0]

    def __draw_body(self):
        # initialize the first 3 segments & Set the start position
        for i in range(3):
            self.__add_part((0, 20 * i))

    def __add_part(self, pos):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(pos)
        self.segments.append(square)

    def extend(self):
        self.__add_part(self.segments[-1].position())

    def move(self):
        """This function controls the moving logic of the snake object"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """This function moves the snake upwards"""
        # This condition prevents connection of the snake body parts
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """This function moves the snake downwards"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """This function moves the snake left"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """This function moves the snake right"""
        if self.head.heading() != 180:
            self.head.setheading(0)
