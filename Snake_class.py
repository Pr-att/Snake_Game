from turtle import *

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for x in STARTING:
            self.add_segment(x)

    def add_segment(self, x):
        tim = Turtle(shape='square')
        tim.color('white')
        tim.penup()
        tim.goto(x)
        self.snake_list.append(tim)

    def reset(self):
        for i in self.snake_list:
            i.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[i - 1].xcor()
            new_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)


