from turtle import Turtle


class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")

        self.penup()
        self.speed("fastest")
        self.goto(275, 275)
        self.pendown()
        for i in range(0, 4):
            self.right(90)
            self.forward(550)
        self.hideturtle()

