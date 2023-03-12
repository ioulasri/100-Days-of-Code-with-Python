from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.y_cor = -280

    def start(self):
        self.goto(x=0, y=self.y_cor)

    def go_up(self):
        self.y_cor += 10
        self.goto(x=0, y=self.y_cor)

    def go_back(self):
        self.y_cor = -280
        self.goto(x=0, y=self.y_cor)