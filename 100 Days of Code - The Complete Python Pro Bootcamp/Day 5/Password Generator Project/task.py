from ctypes import pythonapi
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw_as_list = []

print("Welcome to the PyPassword Generator!")
#receive number of chaacters needed from each list, converting to an integer
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#create three new list variables and use random.choices to randomise from the earlier lists
random_letters = random.choices(letters, k=nr_letters)
random_nums = random.choices(numbers, k=numbers)
random_symbs = random.choices(symbols, k=symbols)

# stitch these together into a single list
password_list = random_letters + random_symbs + random_nums

#randomise this using the random.shuffle function
random.shuffle(password_list)
#convert this to a string using the join function
random_password = "".join(password_list)

print(random_password)


