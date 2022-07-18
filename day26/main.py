import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

phonetic_list = [nato_alphabet_dict[letter] for letter in (input("Enter a word:")).upper()]

print(phonetic_list)
