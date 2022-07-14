from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.level = 0

    def update_level(self):
        self.clear()
        self.level += 1
        self.setposition(-210, 260)
        self.write(f"Level: {self.level}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", font=FONT, align=ALIGNMENT)
