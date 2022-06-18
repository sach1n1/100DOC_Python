import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

item = [rock, paper, scissors]

print("What do you choose:\n"
      "Stone: 0\n"
      "Paper: 1\n"
      "Scissor: 2\n")
choice = int(input("Choice:"))


if choice < 3:
    print(item[choice])
    comp = random.randint(0, 2)
    print(f"Computer chose:\n{item[comp]}")
    if choice == comp:
        print("It's a draw.")
    else:
        if (choice == 0 and comp != 1) or (choice == 1 and comp != 2) or (choice == 2 and comp != 0):
            print("You won!")
        else:
            print("Computer won!")
else:
    print("Invalid Entry: You Lost!!!")


