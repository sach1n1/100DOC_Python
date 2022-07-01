import random
import art
from data import data
import os

clear = lambda: os.system('clear')


def clear_and_print_logo():
    clear()
    print(art.logo)


def compare(answer, a_followers, b_followers, count):
    clear_and_print_logo()
    if a_followers > b_followers and answer == "A":
        count += 1
        print(f"You're right! Current score: {count}.")
        return True, count
    elif a_followers < b_followers and answer == "B":
        count += 1
        print(f"You're right! Current score: {count}.")
        return True, count
    else:
        print(f"Sorry, that's wrong. Final score: {count}.")
        return False, count


def display_comparisons(element_a, element_b, count):
    print(f"A: {element_a['name']}, {element_a['description']} from {element_a['country']}")
    print(art.vs)
    print(f"B: {element_b['name']}, {element_b['description']} from {element_b['country']}")
    print(element_a['follower_count'],
                   element_b['follower_count'])
    return compare(input("Who has more followers? Type 'A' or 'B':").upper(),
                   element_a['follower_count'],
                   element_b['follower_count'],
                   count)


def game():
    clear_and_print_logo()
    random.shuffle(data)
    correct_answer = True
    number_of_correct_answers = 0

    while len(data) > 1 and correct_answer != False:
        a = data.pop(0)
        b = data[0]
        correct_answer, number_of_correct_answers = display_comparisons(a, b, number_of_correct_answers)

    if correct_answer:
        clear_and_print_logo()
        print("You have won the game.")


game()
