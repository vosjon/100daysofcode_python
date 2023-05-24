# Day 8 of 100 - Caesar Cipher

import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    plain_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            plain_text += alphabet[position + shift]
        elif direction == "decode":
            plain_text += alphabet[position - shift]
    
    print(f"The {direction}d text is {plain_text}")

print(art.logo)

keep_going = True

while (keep_going):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    go_again = input("Would you like to go again? Yes or No:\n").lower()
    if go_again == "no":
        keep_going = False
    else:
        continue

print("Goodbye, thanks for playing.")
