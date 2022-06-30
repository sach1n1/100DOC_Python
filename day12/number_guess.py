import random
from art import logo

print(logo)

print("Welcome to the Number Guess game!")

HARD_LEVEL_TRIES = 10
EASY_LEVEL_TRIES = 5


def set_level(input_level):
    if input_level == "easy":
        return HARD_LEVEL_TRIES
    elif input_level == "hard":
        return EASY_LEVEL_TRIES
    else:
        print("Wrong input.")
        return set_level(input("Choose a difficulty: Type 'easy' or 'hard':").lower())


def check_guess(guessed, actual):
    if guessed > actual:
        print("Too High!")
    elif guessed == actual:
        print("You have found the number!")
    else:
        print("Too Low!")


lower_limit = random.randint(0, 100)
upper_limit = random.randint(lower_limit + 100, lower_limit + 200)
number = random.randint(lower_limit, upper_limit)
print(f"I am thinking of a number between {lower_limit} and {upper_limit}.")
tries = set_level(input("Choose a difficulty: Type 'easy' or 'hard':").lower())

guess = None

while tries > 0 and guess != number:
    print(f"you have {tries} tries remaining to guess the number.")
    guess = int(input("Make a guess:"))
    check_guess(guess, number)
    tries -= 1

if tries == 0:
    print("You have run out of guesses. You lose!!")
