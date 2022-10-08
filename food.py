from turtle import *
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('orange')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        random_food_x = random.randint(-280, 270)
        random_food_y = random.randint(-280, 270)
        self.goto(random_food_x, random_food_y)
        self.refresh()

    def refresh(self):
        random_food_x = random.randint(-280, 270)
        random_food_y = random.randint(-280, 270)
        self.goto(random_food_x, random_food_y)