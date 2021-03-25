import random
from db import letters, numbers, symbols

print("Welcome to the the Simple Password Generator!")
nr_letters = int(input("How many letters would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

random.shuffle(password)

strong_pass = ""
for letter in password:
    strong_pass += letter

print(f"Your Simple Secure Password is: {strong_pass}")
