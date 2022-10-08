import time
from turtle import *
from Snake_class import Snake
from food import Food
from Scoreboard import Scoreboard


tim = Turtle()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.title('Pratt Snake Game')
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.snake_list[0].xcor() > 280 or snake.snake_list[0].xcor() < -280 or snake.snake_list[0].ycor() > 270 or snake.snake_list[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for i in snake.snake_list[1:]:
        if snake.snake_list[0].distance(i) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
