from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from outline import Outline
import time

# Screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# creating objects needed
snake = Snake()
food = Food()
score = Score()
outline = Outline()

state_of_game = True

# Getting input from user
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# Outline cordinnates
x_cords = outline.outline_xcor()
y_cords = outline.outline_ycor()

while state_of_game:
    time.sleep(0.05)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.regen()
        score.increment()
        snake.add_length()
    if snake.head.xcor() < x_cords[0] or snake.head.xcor() > x_cords[1] or snake.head.ycor() < y_cords[0] or snake.head.ycor() > y_cords[1]:
        state_of_game = False
        snake.clear_snake_parts()
        score.game_finished()
    for part in snake.snake_parts[1:] :
        if snake.head.distance(part) < 5:
            state_of_game = False
            snake.clear_snake_parts()
            score.game_finished()
    screen.update()
screen.exitonclick()
