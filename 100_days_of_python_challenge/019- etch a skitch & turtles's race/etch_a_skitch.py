from turtle import Turtle, Screen

ninja_turtle = Turtle()
screen = Screen()
ninja_turtle.shape("turtle")
is_forward = True


def move_forward():
    ninja_turtle.forward(10)
    global is_forward
    if not is_forward:
        ninja_turtle.tilt(180)
        is_forward = True


def move_backward():
    ninja_turtle.backward(10)
    global is_forward
    if is_forward:
        ninja_turtle.tilt(180)
        is_forward = False


def move_left():
    ninja_turtle.left(90)


def move_right():
    ninja_turtle.right(90)


def clear():
    ninja_turtle.clear()
    ninja_turtle.penup()
    ninja_turtle.home()
    ninja_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear())
screen.exitonclick()
