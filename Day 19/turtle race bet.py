import random
from turtle import Turtle, Screen


def race():
    for i in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(x=-450, y=y[i])
        turltes.append(new_turtle)


screen = Screen()
screen.setup(width=1000, height=500)
screen.title("Race bet")
screen.bgcolor("black")
user_bet = screen.textinput(title="Make your bet", prompt="Which color do you think will win the race: ")
turltes = []
race_on = False
colors = ["red", "yellow", "green", "orange", "blue", "purple"]
y = [-70, -40, -10, 20, 50, 80]
race()

if user_bet:
    race_on = True

while race_on:
    for turlte in turltes:
        if turlte.xcor() > 460:
            race_on = False
            if user_bet == turlte.pencolor():
                play_again = screen.textinput(f"You won the bet", "Do you want to play again?(yes or no): ").lower()
                if play_again == "yes":
                    screen.clear()
                    race_on = True
                    race()
                else:
                    screen.bye()
            else:
                print("You lost the bet\nThe winner is " + str(turlte.pencolor()))
                play_again = screen.textinput(f"You lost the bet", "Do you want to play again?(yes or no): ").lower()
                if play_again == "yes":
                    screen.clear()
                    race_on = True
                    race()
                else:
                    screen.bye()
        speed = random.randint(1, 10)
        turlte.forward(speed)

screen.exitonclick()
