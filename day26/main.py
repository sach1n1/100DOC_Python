import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def nato_phonetic_list():
    name = input("Enter a word:").upper()
    try:
        phonetic_list = [nato_alphabet_dict[letter] for letter in name]
    except KeyError:
        print("Only letters in the name please!")
        nato_phonetic_list()
    else:
        print(phonetic_list)


nato_phonetic_list()
