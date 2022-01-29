from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from outline import Outline
import time

# Screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.title('Snake Game')


def snake_game():
    screen.tracer(0)
    screen.bgcolor('black')
    
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
    screen.onkey(screen.bye, 'Escape')

    # Outline cordinnates
    x_cords = outline.outline_xcor()
    y_cords = outline.outline_ycor()
    
    while state_of_game:
        time.sleep(0.07)
        snake.move_snake()
        if snake.head.distance(food) < 15:
            food.regen()
            score.increment()
            snake.add_length()
        if snake.head.xcor() < x_cords[0] or snake.head.xcor() > x_cords[1] or snake.head.ycor() < y_cords[0] or snake.head.ycor() > y_cords[1]:
            state_of_game = False
            snake.clear_snake_parts()
            score.game_finished()
        for part in snake.snake_parts[1:]:
            if snake.head.distance(part) < 5:
                state_of_game = False
                snake.clear_snake_parts()
                score.game_finished()
        screen.update()
        
    # prompt user to choose to restart the game
    if state_of_game == False:
        answer = screen.textinput('GAME OVER', 'Would you like to play again?(y/n)')
        if answer == 'y':
            screen.clearscreen()
            snake_game()
        else:
            screen.bye()
snake_game()
screen.exitonclick()
