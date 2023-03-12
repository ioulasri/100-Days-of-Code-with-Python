from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("black")

    def update_score(self, a, x, y):
        self.goto(x, y)
        self.write(arg=a, move=False, align=ALIGN, font=FONT)
