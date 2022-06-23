import random
from art import stages, logo
from words import word_list

print(logo)

chosen_word = random.choice(word_list)


guess_list = []
guessed_letters = []
lives = 6

for letter in chosen_word:
    guess_list.append("_")

while '_' in guess_list and lives > 0:
    guess = input("Guess a letter?").lower()
    if guess not in guessed_letters:
        if len(guess) == 1 and guess in chosen_word:
            for index in range(len(chosen_word)):
                if guess == chosen_word[index]:
                    guess_list[index] = guess
        else:
            print(f"{guess} not in the word. You lose a life!")
            lives -= 1
        print(stages[lives])
        print(f"{' '.join(guess_list)}")
        guessed_letters += guess
    else:
        print(f"{guess} has already been guessed!")

if lives != 0:
    print("You Won!")
else:
    print("You Lost!!")
    print(f"The word is {chosen_word}")
