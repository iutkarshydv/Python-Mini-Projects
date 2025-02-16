print("Welcome to the treasure island")
a=input("Left or Right?").lower()
b=""
c=""

if a=="right":
    print("Game Over")
elif a=="left":
    b=input("swim or wait?").lower()

if b=="swim":
    print("Game Over")
elif b=="wait":
    c=input("Which door, Red, Blue or Yellow?").lower()

if c=="red":
    print("Game Over")
elif c=="blue":
    print("Game Over")
elif c=="yellow":
    print("You Win")