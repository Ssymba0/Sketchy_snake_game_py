from turtle import Turtle
import pickle
from os import path

alignment = 'center'
font = ('Calibri', 20, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.up()
        self.goto(0, 260)
        self.high_score = 0
        self.current_score = 0
        self.import_highscore()
        self.update_scoreboard()

    def import_highscore(self):
        if path.exists('.\Snake_game\high_score.txt'):
            if path.getsize('.\Snake_game\high_score.txt'):
                with open('.\Snake_game\high_score.txt', 'rb') as f:
                    self.high_score = pickle.load(f)
            else:
                return
        else:
            with open('.\Snake_game\high_score.txt', 'xb+') as f:
                pickle.dump(self.high_score, f)

    def reset_score(self):
        self.current_score = 0
        self.update_scoreboard()

    def increment(self):
        self.current_score += 1
        self.highest_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f'Score = {self.current_score} High score = {self.high_score}', align=alignment, font=font)

    def highest_score(self):
        self.clear()
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open(".\Snake_game\high_score.txt", 'wb+') as f:
                pickle.dump(self.high_score, f)
        self.update_scoreboard()

    def game_finished(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', align=alignment, font=font)
        self.goto(0, -30)
        self.write(
            f'Your final score = {self.current_score}', align=alignment, font=font)
        self.goto(0, -60)
        self.write(
            f'Your Highest Score = {self.high_score}', align=alignment, font=font)
