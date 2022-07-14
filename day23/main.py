import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

scoreboard.update_level()

game_is_on = True

while game_is_on:

    car_manager.create_car()
    car_manager.move()
    time.sleep(0.1)
    screen.update()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.reached_other_side():
        car_manager.increase_speed()
        scoreboard.update_level()


screen.exitonclick()
