from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encode(text, shift):
#     encoded_message = ""
#     for letter in text:
#         index_of_letter = alphabet.index(letter)
#         new_index = (index_of_letter + shift) % len(alphabet)
#         encoded_message += alphabet[new_index]
#     print(f"The encoded message is {encoded_message}")
#
#
# def decode(text, shift):
#     decoded_message = ""
#     for letter in text:
#         index_of_letter = alphabet.index(letter)
#         new_index = index_of_letter - shift
#         decoded_message += alphabet[new_index]
#     print(f"The decoded message is  {decoded_message}")

def caesar(direction, text, shift):
    output_message = ""
    for letter in text:
        if letter.isalpha():
            index_of_letter = alphabet.index(letter)
            if direction == "decode":
                new_index = index_of_letter - shift
            else:
                new_index = (index_of_letter + shift) % len(alphabet)
            output_message += alphabet[new_index]
        else:
            output_message += letter
    print(f"The {direction}d message is {output_message}")


print(logo)

continue_cipher = "yes"

while continue_cipher == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
    else:
        print(f"Your input {direction} is wrong!")

    continue_cipher = input("Do you want to continue using the cipher?\nType yes or no:").lower()

print("Goodbye.")
