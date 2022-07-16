import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=720, height=510)
screen.title("US States Game")
screen.addshape("blank_states_img.gif")

state = pd.read_csv("50_states.csv")

turtle.shape("blank_states_img.gif")

guessed_states = []
score = 0

while score < 50:
    guess_input = screen.textinput(title="Guess the state!", prompt=f"({score}/50) Guess another state's name?").title()
    if guess_input == "Exit":
        break
    data = state[state.state == guess_input]
    if not data.empty:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(int(data.x), int(data.y))
        pen.write(guess_input)
        score += 1
        guessed_states.append(guess_input)


for guess in guessed_states:
    state = state.drop(state[state.state == guess].index)

state = state.reset_index(drop=True)

state.to_csv("States_to_learn.csv")

# screen.exitonclick()
