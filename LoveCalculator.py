name=input("Enter your name: ")
name3=input("Enter their name: ")

name1=name.lower()
name2=name3.lower()

t=name1.count("t") + name2.count("t")
r=name1.count("r") + name2.count("r")
u=name1.count("u") + name2.count("u")
e=name1.count("e") + name2.count("e")

l=name1.count("l") + name2.count("l")
o=name1.count("o") + name2.count("o")
v=name1.count("v") + name2.count("v")

true=t+r+u+e
love=l+o+v+e

print(f"Your love score is {true}{love}")
