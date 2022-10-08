from turtle import *
title_co_x = -20
title_co_y = 270


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.score_from_text())
        self.color('white')
        self.penup()
        self.goto(title_co_x, title_co_y)
        self.hideturtle()
        self.update_scoreboard()

    def score_from_text(self):
        with open('data.txt') as f:
            content = f.read()
            return content

    def increase_score_from_text(self):
        with open('data.txt', mode='w') as g:
            g.write(f'{self.score}')

    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE: {self.score} \t High Score: {self.score_from_text()}', move=False, align="center", font=("times new roman", 14, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.increase_score_from_text()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()