import time
from turtle import Screen
from day20.SnakeClass import Snake
from day20.food import Food
from day20.scoreboard import Scoreboard
from day20.boundary import Boundary

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
boundary = Boundary()
food = Food()
score = Scoreboard()
score.update_score()


screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_length[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        score.update_score()

    if snake.snake_length[0].xcor() < -275 or  \
       snake.snake_length[0].xcor() > 275 or  \
       snake.snake_length[0].ycor() < -275 or \
       snake.snake_length[0].ycor() > 275:
        # game_is_on = False
        score.reset()
        snake.reset()
        #score.game_over()

    for segment in snake.snake_length[1:]:
        if snake.snake_length[0].distance(segment) < 5:
            # game_is_on = False
            score.reset()
            snake.reset()
            #score.game_over()


screen.exitonclick()
