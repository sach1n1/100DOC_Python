from turtle import Turtle

FONT = ('Courier', 18, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.score = -1

    def update_score(self):
        self.clear()
        self.score += 1
        self.setposition(0, 275)
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", font=FONT, align=ALIGNMENT)


