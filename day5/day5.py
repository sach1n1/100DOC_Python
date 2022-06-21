#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=''

for char in range(0, nr_letters+nr_symbols+nr_numbers):
    if char < nr_letters:
        letter = random.randint(0, len(letters)-1)
        password += letters[letter]
    elif char < nr_letters + nr_symbols:
        symbol = random.randint(0, len(symbols)-1)
        password += symbols[symbol]
    else:
        number = random.randint(0, len(numbers)-1)
        password += numbers[number]

#random_pass = ''.join(random.sample(password, len(password)))

random_pass = ''

for char in random.sample(password, len(password)):
    random_pass += char

print(f"Easy Password: {password}")
print(f"Hard Password: {random_pass}")

