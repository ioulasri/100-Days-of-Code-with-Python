import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        r = random.randint(-270, 270)
        t = random.randint(-270, 270)
        self.goto(r, t)
