import random
from turtle import Screen
import time
from player import Player
from cars import Car
from score_board import Score
cars = []
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("The crossing turtle game")
screen.tracer(0, 0)
player = Player()
player.start()
score = Score()
screen.listen()
screen.onkey(player.go_up, "Up")
go = True
a = 0
speed = 0.1
while go:
    time.sleep(speed)
    a = random.randint(1, 10000)
    if 0 < a < 1000:
        car = Car()
        cars.append(car)
    else:
        pass
    for i in cars:
        i.move()

    for caar in cars:
        if caar.distance(player) < 25:
            score.game_over()
            go = False

    if player.ycor() > 280:
        score.increase_score()
        player.go_back()
        speed *= 0.9

    screen.update()

screen.exitonclick()
