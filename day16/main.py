from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
resource = CoffeeMaker()
money = MoneyMachine()


def coffee_machine():
    machine_input = input(f"What would you like? {coffee.get_items()}:").lower()
    if machine_input == "report":
        resource.report()
        money.report()
        coffee_machine()
    elif machine_input == "off":
        return
    elif coffee.find_drink(machine_input) is not None:
        drink = coffee.find_drink(machine_input)
        if resource.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                resource.make_coffee(drink)
                coffee_machine()
        coffee_machine()
    else:
        coffee_machine()


coffee_machine()
