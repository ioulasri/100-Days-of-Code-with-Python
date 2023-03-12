from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="z", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="q", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
