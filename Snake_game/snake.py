from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, i):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for i in self.segments:
            i.goto(x=1000, y=1000)
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

