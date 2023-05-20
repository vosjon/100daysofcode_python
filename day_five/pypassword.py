# Day 5 of 100 - Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

list_letters = random.choices(letters, k=nr_letters)
list_numbers = random.choices(numbers, k=nr_symbols)
list_symbols = random.choices(symbols, k=nr_numbers)
password_list = list_letters + list_numbers + list_symbols
random.shuffle(password_list)
password = "".join(password_list)

print(f"Your new password is: {password}")

# Here are my notes I used to figure out how to solve this:
# 1. Use random.choices(list name, k=number) to pull from each list
# 2. Concatenate all pulled items into a new list
# 3. Use random.shuffle(list name) to shuffle the list
# 4. Create a password variable and the list to a string with "".join(list name)
