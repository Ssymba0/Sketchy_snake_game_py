from turtle import Turtle

class Outline(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(-300, -240)
        self.down()
        self.color('brown')
        self.width(10)
        for i in range(4):
            heading = self.heading()
            if i % 2:
                self.forward(480)
                self.seth(heading + 90)
            else:
                self.forward(600)
                self.seth(heading + 90)
    def outline_xcor(self):
        return (-300,300)
    def outline_ycor(self):
        return (-240,240)