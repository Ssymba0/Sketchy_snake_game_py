from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.speed(0)
        self.regen()

    def regen(self):
        x_cor = random.randint(-290, 290)
        y_cor = random.randint(-230, 230)
        self.goto(x=x_cor, y=y_cor)
