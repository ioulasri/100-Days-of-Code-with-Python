import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG")
screen.tracer(0)
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "z")
screen.onkey(l_paddle.go_down, "s")
a = 0.05
game_on = True
while game_on:
    time.sleep(a)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.x_bounce()
        if a > 0:
            a -= 0.001
        else:
            pass
    if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.x_bounce()
        if a > 0:
            a -= 0.001
        else:
            pass
    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        ball.lost()
        a = 0.05
        r_paddle.goto(370, 0)
        l_paddle.goto(-380, 0)
        score.increase_score("Z")
        score.update_score()
    if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        ball.lost()
        a = 0.05
        l_paddle.goto(-380, 0)
        r_paddle.goto(370, 0)
        score.increase_score("right")
        score.update_score()

screen.exitonclick()
