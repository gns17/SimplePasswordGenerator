from passgen import PassGen

print("Welcome to the the Simple Password Generator!")
letters = int(input("How many letters would you like?\n"))
symbols = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))

pgen = PassGen()
pgen.generate_password(letter=letters, symbol=symbols, number=numbers)

print(f"Your Simple Secure Password is: {pgen.final_password}")
