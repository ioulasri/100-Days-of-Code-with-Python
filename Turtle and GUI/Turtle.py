from turtle import Turtle, Screen
import random

timmy = Turtle()
colors = ["black", "red", "yellow", "orange", "blue", "brown", "pink", "green", "aqua"]
timmy.speed('fastest')


def draw_spawgraph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random.choice(colors))
        timmy.circle(120)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spawgraph(1)

screen = Screen()
screen.exitonclick()
