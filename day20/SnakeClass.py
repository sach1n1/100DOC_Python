from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake_length = []
        self.create_initial_segment()

    def create_initial_segment(self):
        for i in range(0, 3):
            snake_segment = Turtle("square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto((snake_segment.xcor() - i*MOVE_DISTANCE, 0))
            self.snake_length.append(snake_segment)

    def move(self):
        for num in range(len(self.snake_length) - 1, 0, -1):
            self.snake_length[num].goto(self.snake_length[num - 1].position())
        self.snake_length[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake_length[0].heading() != DOWN:
            self.snake_length[0].setheading(UP)

    def move_down(self):
        if self.snake_length[0].heading() != UP:
            self.snake_length[0].setheading(DOWN)

    def move_right(self):
        if self.snake_length[0].heading() != LEFT:
            self.snake_length[0].setheading(RIGHT)

    def move_left(self):
        if self.snake_length[0].heading() != RIGHT:
            self.snake_length[0].setheading(LEFT)

    def add_segment(self):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        last_segment_coordinates = self.snake_length[-1].pos()
        snake_segment.goto(last_segment_coordinates)
        self.snake_length.append(snake_segment)
