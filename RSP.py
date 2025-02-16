import random
print("Let's play Rock Paper Scissors")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user=str(input("Rock, Paper, Scissors?").lower())
cpu=random.randint(0,2)
your_score=0
cpu_score=0

if user=="rock":
    if cpu==0:
        your_score=your_score+0
        cpu_score=cpu_score+0
        print(rock, "\n You")
        print(rock, "\n CPU")
        print("TIE")
    if cpu==1:
        your_score=your_score+0
        cpu_score=cpu_score+1
        print(rock, "\n You")
        print(paper, "\n CPU")
        print("CPU Wins!")
    if cpu==2:
        your_score=your_score+1
        cpu_score=cpu_score+0
        print(rock, "\n You")
        print(scissors, "\n CPU")
        print("You Win!")
elif user=="paper":
    if cpu==0:
        your_score=your_score+1
        cpu_score=cpu_score+0
        print(paper, "\n You")
        print(rock, "\n CPU")
        print("You Win!")
    if cpu==1:
        your_score=your_score+0
        cpu_score=cpu_score+0
        print(paper, "\n You")
        print(paper, "\n CPU")
        print("TIE")
    if cpu==2:
        your_score=your_score+0
        cpu_score=cpu_score+1
        print(paper, "\n You")
        print(scissors, "\n CPU")
        print("CPU Wins!")
elif user=="scissors":
    if cpu==0:
        your_score=your_score+0
        cpu_score=cpu_score+1
        print(scissors, "\n You")
        print(rock, "\n CPU")
        print("CPU Wins!")
    if cpu==1:
        your_score=your_score+1
        cpu_score=cpu_score+0
        print(scissors, "\n You")
        print(paper, "\n CPU")
        print("You Win!")
    if cpu==2:
        your_score=your_score+0
        cpu_score=cpu_score+0
        print(scissors, "\n You")
        print(scissors, "\n CPU")
        print("TIE")

