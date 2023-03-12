from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")
with open("score.txt") as f:
    SC = f.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(SC)
        self.penup()
        self.goto(0, 270)
        self.color("Yellow")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.clear()
        self.goto(-100, 270)
        self.write("Score: " + str(self.score), move=False, align=ALIGN, font=FONT)
        self.goto(100, 270)
        self.write("Highscore: " + str(self.high_score), move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        self.score = 0
