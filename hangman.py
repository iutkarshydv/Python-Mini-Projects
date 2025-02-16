import random
import os
words=["cartoon", "beekeeper", "swimming", "gaming", "running", "random", "working", "elements"]
word=random.choice(words)
split_word=[*word]
stages = ['''
  +---+
  |   |
  O   |
 /| | |
 /  | |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /| | |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /| | |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_  |/ _` | '_  |/ _` | '_ ` _  |/ _` | '_  |
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|*__,_|_| |_|*__, |_| |_| |_|*__,_|_| |_|
                    __/ |                      
                   |___/ ''')
dash=len(word)*"_".split()
hangman=0
print(" ".join(dash))
print(stages[0])
end=False
status="Save Him!"
print(status)
while end==False:
    guess=input("Guess a Letter: ").lower()
    for position in range(len(word)):
        letter=word[position]
        if letter==guess:
            dash[position]=guess # type: ignore
    if guess not in split_word:
        hangman+=1
    if "_" not in dash:
        end=True
        status="You Win"
    if hangman==6:
        status="You Loose"
    os.system('CLS')
    print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_  |/ _` | '_  |/ _` | '_ ` _  |/ _` | '_  |
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|*__,_|_| |_|*__, |_| |_| |_|*__,_|_| |_|
                    __/ |                      
                   |___/ ''')
    print(" ".join(dash))
    print(stages[hangman])
    print(status)
    if status=="You Loose":
        break
