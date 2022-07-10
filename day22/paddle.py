from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.create_paddle(paddle_position)

    def create_paddle(self, paddle_position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=3)
        self.setheading(90)
        self.speed("fast")
        self.penup()
        self.goto(paddle_position)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)
