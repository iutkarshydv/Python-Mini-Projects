import random
import os
number=random.randrange(1,100)
logo='''
   ______                        ______ _            _   __                __             
  / ____/_  _____  __________   /_  __/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/    / / / __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )    / / / / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/    /_/ /_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                          
    '''
os.system('CLS')

print(logo)
attempts=int(input("Choose number of attempts: "))
os.system('CLS')
guess=0
def check(guess,number):
    if guess==0:
        pass 
    elif guess > number:
        print("You are too high")
    elif guess < number:
        print("You are too low")

while not attempts==0:
    print(number)
    print(logo)
    print(f"You have {attempts} attempts left!")
    check(guess,number)
    guess=int(input("Guess a number: "))
    os.system('CLS')
    if guess==number:
        print(logo)
        print("You guessed it right")
        break
    else:
        attempts-=1

if attempts==0:
    print(logo)
    print("You failed to guess the number")