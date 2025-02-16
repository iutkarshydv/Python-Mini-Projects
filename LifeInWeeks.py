a=int(input("Please enter your age: "))
b=a*52.1429
weeks=(90*52.1429)-b
months=weeks/4.34524
days=((months/2)*30)+((months/2)*31)
print(f"You have {int(weeks)} weeks, {int(months)} months, {int(days)} days left to live")