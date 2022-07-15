from turtle import Turtle
import os.path

FONT = ('Courier', 18, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.high_score = 0
        self.get_high_score()
        self.score = -1

    def update_score(self):
        self.clear()
        self.score += 1
        self.setposition(0, 275)
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        file = open("high_score.txt", "w")
        file.write(f"{self.high_score}")
        self.score = -1
        self.clear()
        self.update_score()

    def get_high_score(self):
        if os.path.exists("./high_score.txt"):
            file = open("high_score.txt", "r")
            self.high_score = int(file.read())
            #self.high_score = int(high_score)
            file.close()
        else:
            self.high_score = 0

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("Game Over", font=FONT, align=ALIGNMENT)


