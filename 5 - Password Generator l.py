import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_suggestion = []

#in a real world scenario, you would need to handle input errors.
#such as, not accepting 0 as a value. not accepting incorrect values.

nr_letters = int(input("How many letters would you like your password to be?\n"))
nr_numbers = int(input("How many symbols would you like your password to be?\n"))
nr_symbols = int(input("How many numbers would you like your password to be?\n"))

for i in range(nr_letters):
    password_suggestion.append(random.choice(letters))

for i in range(nr_numbers):
    password_suggestion.append(random.choice(numbers))

for i in range(nr_symbols):
    password_suggestion.append(random.choice(symbols))

random.shuffle(password_suggestion)
complete_password = ''.join(password_suggestion)
print(f"Your password is: {complete_password}")