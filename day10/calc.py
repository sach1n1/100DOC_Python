from calc_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num_initial = float(input("Enter first number:"))
    for symbol in operation:
        print(symbol)

    continue_calc = "yes"

    while continue_calc == "yes":
        op = input("Choose an operation from above:")
        num_next = float(input("Enter next number:"))
        result = operation[op](num_initial, num_next)
        print(f"{num_initial} {op} {num_next} = {result}")
        num_initial = result
        continue_calc = input(f"Type yes to continue calculations with {result}."
                              f"\nType no to start a new calculation."
                              f"\nType x to exit."
                              f"\nYour input:").lower()
    if continue_calc == 'x':
        return 0
    else:
        calculator()


calculator()
