from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-230, 270)
        self.color("black")
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.write("score: " + str(self.score), move=False, align=ALIGN, font=FONT)
