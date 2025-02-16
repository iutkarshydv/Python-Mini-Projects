import os

row1=["✉️", "✉️", "✉️"]
row2=["✉️", "✉️", "✉️"]
row3=["✉️", "✉️", "✉️"]

nested_rows=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
x=input("Where do you wanna place the treasure?(mn)")

row=int(x[0])-1
column=int(x[1])-1

nested_rows[row][column]="🪙"
os.system('cls')
print(f"{row1}\n{row2}\n{row3}")
