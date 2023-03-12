import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
dif = screen.textinput("Choose a difficulty", "easy ¶ medium ¶ hard").lower()
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_ON = True

while game_ON:
    screen.update()
    if dif == "hard":
        time.sleep(0.05)
    elif dif == "medium":
        time.sleep(0.1)
    elif dif == "easy":
        time.sleep(0.5)
    snake.move()
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        score.increase_score()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            food.refresh()
            score.reset()
            score.update_score()
            snake.reset()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        food.refresh()
        score.reset()
        score.update_score()
        snake.reset()

screen.exitonclick()
