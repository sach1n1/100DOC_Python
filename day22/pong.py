import time
from turtle import Screen
from day22.paddle import Paddle
from day22.ball import Ball
from day22.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = Scoreboard((100, 271))
l_score = Scoreboard((-100, 271))
r_score.update_score()
l_score.update_score()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True

sleep_time = 0.1

while game_is_on:
    time.sleep(sleep_time)

    if ball.distance(r_paddle) < 30 and ball.xcor() < 345\
            or ball.distance(l_paddle) < 30 and ball.xcor() > -345:
        ball.x_move *= -1
        sleep_time /= 1.5

    screen.update()

    if ball.xcor() < -350:
        r_score.update_score()
        ball.reset_position()
        sleep_time = 0.1

    if ball.xcor() > 350:
        l_score.update_score()
        ball.reset_position()
        sleep_time = 0.1

    ball.move()



screen.exitonclick()
