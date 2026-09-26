from string import ascii_letters, digits, punctuation
from itertools import product

value = ascii_letters + digits + punctuation
count = 0

with open("password_warehouse.txt", "a") as file:
    for i in range(3, 4):
        for j in product(value, repeat=i):
            word = "".join(j) + "\n"
            file.write(word)
            count += 1
            print(f"{count} passwords are Generated")