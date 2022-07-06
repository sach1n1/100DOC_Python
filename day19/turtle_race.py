import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
colors = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']

turtles = []

starting_position = (-230, -150)

color = ""


def input_color():
    color = screen.textinput("Select Turtle", "Enter the color of the turtle\n"
                                              "(Violet/Blue/Green/Yellow/Orange/Red):").lower()
    return color


while color not in colors:
    color = input_color()

for i in range(0, len(colors)):
    turtle_object = Turtle("turtle")
    turtle_object.penup()
    turtle_object.color(colors[i])
    turtle_object.goto(starting_position[0], starting_position[1] + i*60)
    turtle_object.speed("fast")
    turtles.append(turtle_object)


def check_coordinates():
    for turtle in turtles:
        if turtle.xcor() > 230:
            if color == turtle.fillcolor():
                print(f"Your bet, the {turtle.fillcolor()} won the race!")
            else:
                print(f"Your bet lost the race! The {turtle.fillcolor()} turtle won the race!")
            return True
    return False


race_finish = False

while not race_finish:
    for turtle in turtles:
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)
    race_finish = check_coordinates()

screen.exitonclick()
