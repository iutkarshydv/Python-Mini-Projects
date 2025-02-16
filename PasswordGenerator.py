import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

l=int(input("Enter how many letters you wanna use"))
n=int(input("Enter how many numbers you wanna use"))
s=int(input("Enter how many symbols you wanna use"))

password=""

for number in range(1, n+1):
    random_ns=random.choice(numbers)
    password+=random_ns

for letter in range(1,l+1):
    random_ls=random.choice(letters)
    password+=random_ls

for symbol in range(1,s+1):
    random_ss=random.choice(symbols)
    password+=random_ss

list_password=list(password)
random.shuffle(list_password)
joined_password="".join(list_password)
print(joined_password)