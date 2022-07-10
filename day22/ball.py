from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize()
        self.color("white")
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        if self.ycor() < -250 or self.ycor() > 250:
            self.y_move = self.y_move*(-1)

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1


