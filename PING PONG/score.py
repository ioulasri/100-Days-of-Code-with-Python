from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 40, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, move=False, align=ALIGN, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, move=False, align=ALIGN, font=FONT)

    def increase_score(self, side):
        if side == "right":
            self.r_score += 1
            self.update_score()
        else:
            self.l_score += 1
            self.update_score()
