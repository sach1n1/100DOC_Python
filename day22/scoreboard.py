from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.position = position
        self.hideturtle()
        self.score = -1

    def update_score(self):
        self.clear()
        self.score += 1
        self.setposition(self.position)
        self.write(f"{self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", font=FONT, align=ALIGNMENT)


