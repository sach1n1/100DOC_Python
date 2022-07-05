import random
import colorgram
from turtle import Turtle, Screen, colormode

tim = Turtle()
tim.hideturtle()
screen = Screen()
tim.width(10)
tim.speed("fastest")

colormode(255)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)


colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
          (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
          (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
          (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tim.setheading(225)
tim.penup()
tim.forward(550)
tim.setheading(0)
pos = tim.pos()

for i in range(1, 11):
    for _ in range(1, 11):
        tim.pendown()
        tim.color(random.choice(colors))
        tim.dot()
        tim.penup()
        tim.forward(80)
    tim.goto(pos[0], pos[1] + i*80)

screen.exitonclick()
