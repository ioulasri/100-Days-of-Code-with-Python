import random
from turtle import Turtle
import time

COLORS = ["red", "pink", "purple", "yellow", "orange", "blue", "green", "cyan"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.y = random.randint(-250, 270)
        self.x = 280
        self.goto(x=self.x, y=self.y)
        self.move()

    def move(self):
        self.x -= 10
        self.goto(x=self.x, y=self.y)
