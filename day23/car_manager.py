import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        while random.randint(1, 6) == 6:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            position = random.randint(-250, 250)
            car.setpos(300, position)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
