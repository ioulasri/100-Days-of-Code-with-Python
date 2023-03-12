import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")


def generator():
    nr_letters = 5
    nr_symbols = 4
    nr_numbers = 4

    password = ""

    for i in range(nr_letters + 1):
        password += random.choice(letters)
    for j in range(nr_numbers + 1):
        password += random.choice(numbers)
    for e in range(nr_symbols + 1):
        password += random.choice(symbols)

    str_var = list(password)
    random.shuffle(str_var)

    return ''.join(str_var)


print(generator())
