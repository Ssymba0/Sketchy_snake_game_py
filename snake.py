from turtle import Turtle
import time

position = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]
        
    def create_snake(self):
        for pos in position:
            snake = Turtle('square')
            snake.shapesize(stretch_len=0.5, stretch_wid=0.5)
            snake.up()
            snake.color('white')
            snake.goto(pos)
            self.snake_parts.append(snake)

    def move_snake(self):
        for num in range(len(self.snake_parts) - 1, 0, -1):
            x_cor = self.snake_parts[num - 1].xcor()
            y_cor = self.snake_parts[num - 1].ycor()
            self.snake_parts[num].goto(x_cor, y_cor)
        self.head.fd(10)

    def up(self):
        if self.head.heading() != down:
            self.head.seth(up)

    def down(self):
        if self.head.heading() != up:
            self.head.seth(down)

    def left(self):
        if self.head.heading() != right:
            self.head.seth(left)

    def right(self):
        if self.head.heading() != left:
            self.head.seth(right)
    
    def add_length(self):
        new_part = Turtle('square')
        new_part.color('white')
        new_part.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_part.up()
        # x_cor = self.snake_parts[-1].xcor()
        # y_cor = self.snake_parts[-1].ycor()
        # new_part.goto(x_cor, (y_cor + 20 if y_cor > 0 else y_cor -20))
        new_part.goto(self.snake_parts[-1].position())
        self.snake_parts.append(new_part)
    def clear_snake_parts(self):
        for snake in self.snake_parts:
            snake.hideturtle()