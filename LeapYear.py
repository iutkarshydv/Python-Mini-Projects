a=int(input("Enter the year:-"))
def leap(year):
    if year%4==0 & year%100==0 & year%400==0:
        return True
    elif year%4==0 & year%100!=0:
        return True
    elif year%4==0 & year%100==0 & year%400!=0:
        return False
    elif year%4!=0:
        return False
print(f"Leap Year: {leap(a)}")