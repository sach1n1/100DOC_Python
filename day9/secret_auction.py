from art import logo
import os

clear = lambda: os.system('clear')


def find_winner(auction_bidders):
    final_bid = 0
    winner = ""
    for name in bidders:
        if final_bid < auction_bidders[name]:
            final_bid = auction_bidders[name]
            winner = name
    print(f"The winner is {winner} with a bid of ${final_bid}")


clear()
print(logo)
print("Welcome to the secret auction program.")


bidders = {}
more_bidders = "yes"

while more_bidders == "yes":
    name = input("What is you name?")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    more_bidders = input("Are there more bidders? Type yes or no:").lower()
    clear()

find_winner(bidders)
