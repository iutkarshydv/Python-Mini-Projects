height=float(input("Please Enter Your Height(Meters)"))
weight=float(input("Please enter your weight"))

BMI=weight/(height**2)

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are Underweight.")
elif BMI > 18.5 <= 25:
    print(f"Your BMI is {BMI}, you are Normal.")
elif BMI > 25 <= 30:
    print(f"Your BMI is {BMI}, you are Overweight.")
elif BMI > 30 <= 35:
    print(f"Your BMI is {BMI}, you are Obese.")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are Critically Obese.")