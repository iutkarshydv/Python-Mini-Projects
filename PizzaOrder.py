print("Welcome to the pizza order service")
size=input("What size of pizza you want?, S, M or L")
add_pepperoni=input("Do you want pepperoni?, Y or N")
extra_cheese=input("Do you want extra cheese?, Y or N")

cost=0

if size=="S":
    cost=cost+2
elif size=="M":
    cost=cost+3
elif size=="L":
    cost=cost+4

if add_pepperoni=="Y":
    cost=cost+2
else:
    cost=cost+0

if extra_cheese=="Y":
    cost=cost+1
else:
    cost=cost+0

print(f"Your total cost is ${cost}")