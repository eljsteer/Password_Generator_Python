#Password Generator Project
import random

lowercase = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
uppercase = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '@', '&', '^', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_characters = int(input("How many characters would you like in your password?\n"))
upper_choice = input('Would you like uppercase characters? "Y" for Yes, "N" for No\n')
numbers_choice = input('Would you like numbers? "Y" for Yes, "N" for No\n')
symbols_choice = input('Would you like symbols? "Y" for Yes, "N" for No\n')

char_list = lowercase

if upper_choice.lower() == "y":
    char_list += uppercase
if numbers_choice.lower() == "y":
    char_list += numbers
if symbols_choice.lower() == "y":
    char_list += symbols

randomise_list = random.sample(char_list, len(char_list))

p_length = 0

password_result = []

while p_length < nr_characters:
    p_length = p_length + 1
    random.shuffle(randomise_list)
    index_char = random.randint(0, len(char_list) + 1)
    chosen_char = char_list[index_char - 1]
    password_result += chosen_char

password =""
for char in password_result:
  password += char

print(f"Your new Password is: {password}")