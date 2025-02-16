import random

name_list=input("Write the first names seperated with commas?")
names=name_list.split(",")
payee=random.choice(names)

print(f"{payee} will pay the bill today.")