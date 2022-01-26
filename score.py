from turtle import Turtle

alignment = 'center'
font = ('Calibri', 20, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.up()
        self.goto(0,260)
        self.current_score = 0
        self.write(f'Score = {self.current_score}', align=alignment,font=font)
    
    def increment(self):
        self.clear()
        self.current_score += 1
        self.write(f'Score = {self.current_score}', align=alignment,font=font)
    def game_finished(self):
        self.clear()
        self.goto(0,0)
        self.write('GAME OVER', align=alignment, font=font)
        self.goto(0, -30)
        self.write(f'Your final score = {self.current_score}', align=alignment,font=font)