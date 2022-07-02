from resources import MENU, resources

money = 0.0


def take_input():
    coffee_type = ""
    while coffee_type not in MENU:
        coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()
        if coffee_type == "report":
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Water: {resources['water']}ml")
            print(f"Money: ${money}")
        elif coffee_type not in MENU:
            print("Your input is wrong! Try Again!")
    return coffee_type


def check_resources(coffee):
    not_enough = False
    for resource in resources:
        if MENU[coffee]["ingredients"][resource] > resources[resource]:
            print(f"Sorry not enough {resource}!")
            not_enough = True
        else:
            resources[resource] -= MENU[coffee]["ingredients"][resource]
    if not_enough:
        return False
    else:
        return True


def process_transactions(coffee_type):
    global money
    money_received = 0
    coins_values = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }
    for coin in coins_values:
        number_of_coins = int(input(f"How many {coin}?"))
        money_received += number_of_coins * coins_values[coin]
    if money_received < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if money_received > MENU[coffee_type]["cost"]:
            change = money_received - MENU[coffee_type]["cost"]
            print(f"Here's your ${change} in change")
        print(f"Here's your {coffee_type}. Enjoy!! ")
        money += MENU[coffee_type]["cost"]


def coffee_machine():
    choice = take_input()
    sufficient_resources = check_resources(choice)
    if sufficient_resources:
        process_transactions(choice)


while True:
    coffee_machine()
