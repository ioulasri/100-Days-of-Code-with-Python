from turtle import Turtle, Screen
import write
import pandas

screen = Screen()
screen.title("U.S. states game")
screen.setup(width=730, height=495)
ALIGN = "center"
score = write.Score()
FONT = ("Courier", 8, "normal")
image = "blank_states_img.gif"
screen.addshape(image)
tim = Turtle()
tim.shape(image)
correct = 0
data = pandas.read_csv("50_states.csv")
x = data["x"].tolist()
y = data.y.tolist()
states = data["state"].tolist()
states_found = []
playing = True
while playing:
    answer = screen.textinput(f"{correct}/50 states", "What's the name of a state: ").lower()
    if answer.title() in states:
        if answer not in states_found:
            correct += 1
            states_found.append(answer)
            print(answer.title())
            r = x[states.index(answer.title())]
            v = y[states.index(answer.title())]
            score.update_score(answer, r, v)
        else:
            pass
    else:
        pass

screen.exitonclick()
