#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_user = int(input("How many letters would you like in your password?\n")) 
symbols_user = int(input(f"How many symbols would you like?\n"))
numbers_user = int(input(f"How many numbers would you like?\n"))

password = []

for char in range(1, letters_user + 1):
  password.append(random.choice(letters))

for char in range(1, symbols_user + 1):
  password += random.choice(symbols)

for char in range(1, numbers_user + 1):
  password += random.choice(numbers)

random.shuffle(password)

password_gen = ""
for char in password:
  password_gen += char

print(f"Your password is: {password_gen}")
