
file_names = open("./Input/Names/invited_names.txt", "r")
list_of_names = file_names.readlines()
file_names.close()

letter_template_file = open("./Input/Letters/starting_letter.txt", "r")
letter_template = letter_template_file.read()
letter_template_file.close()

for name in list_of_names:
    name = name.strip('\n')
    letter = letter_template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as invitation_letter:
        invitation_letter.write(letter)
