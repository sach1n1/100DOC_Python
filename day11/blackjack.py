############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################################################################

import random
from blackjack_art import logo
import os

clear = lambda: os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_black_jack(dealers_cards, players_cards, end_game):
    if sum(dealers_cards) == 21:
        print(f"Dealer has Blackjack!!"
              f"\nDealers hand: {dealers_cards}")
        print("You Lose!")
        return True
    elif sum(players_cards) == 21:

        print(f"You have Blackjack!!"
              f"\nYour Hand: {players_cards}")
        print("You Win")
        return True
    else:
        return False


def ace_check(cards_in_hand):
    if 11 in cards_in_hand and sum(cards_in_hand) > 21:
        cards_in_hand[cards_in_hand.index(11)] = 1
        return cards_in_hand
    else:
        return cards_in_hand


def black_jack():
    clear()
    print(logo)
    end_game = False
    continue_draw = ""

    dealers_cards = random.choices(cards, k=2)
    players_cards = random.choices(cards, k=2)

    ace_check(players_cards)
    ace_check(dealers_cards)

    print(f"Dealer's Cards: {dealers_cards[0]}")
    print(f"Your Card's: {players_cards}, Current Score = {sum(players_cards)}")

    end_game = check_black_jack(dealers_cards, players_cards, end_game)

    if not end_game:
        continue_draw = input("Type 'y' to get another card, type 'n' to pass:").lower()

    while continue_draw == "y" and not end_game:
        players_cards.append(random.choice(cards))
        players_cards = ace_check(players_cards)
        print(f"Dealer's Card: {dealers_cards[0]}")
        print(f"Your Card's: {players_cards}, Current Score = {sum(players_cards)}")
        if sum(players_cards) > 21:
            print("You Lose")
            end_game = True
        else:
            continue_draw = input("Type 'y' to get another card, type 'n' to pass:").lower()

    while sum(dealers_cards) < 17 and not end_game:
        dealers_cards.append(random.choice(cards))
        print(f"Dealer's Cards: {dealers_cards}, Current Score = {sum(dealers_cards)}")
        print(f"Your Card's: {players_cards}, Current Score = {sum(players_cards)}")
        if sum(dealers_cards) > 21:
            print("Computer Loses")
            end_game = True

    if not end_game:
        if sum(dealers_cards) > sum(players_cards):
            print("You Lose")
        elif sum(dealers_cards) == sum(players_cards):
            print("It's a draw")
        else:
            print("You win")

    play_black_jack()


def play_black_jack():
    continue_black_jack = input("Do you want to play a game of Blackjack. Type yes or no:").lower()
    if continue_black_jack == "yes":
        black_jack()
    else:
        return


clear()
play_black_jack()
