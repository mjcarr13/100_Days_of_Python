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

import random
import sys
options = [0, 1, 2]
#rock = 0, paper = 1, scissors = 2

choice = int(input("It's time for ROCK, PAPER, SCISSORS!!!!\n"
                "For Rock, choose 0\n"
                "For Paper, choose 1\n"
                "For Scissors, chose 2\n"
                "May the odds be ever in your favour!\n"))
if choice <0 or choice >2:
    print("Invalid number, try again!")
    sys.exit(1)
elif choice == 0:
    print(f"You chose rock {rock}")
elif choice == 1:
    print(f"You chose paper {paper}")
elif choice == 2:
    print(f"You chose scissors {scissors}")
computer_choice = random.choice(options)
if computer_choice == 0:
    print(f"Computer chose rock {rock}")
elif computer_choice == 1:
    print(f"Computer chose paper {paper}")
else:
    print(f"Computer chose scissors {scissors}")

if choice == 0 and computer_choice == 0:
    print("It's a draw!")
elif choice == 0 and computer_choice == 1:
    print("Paper beats rock, Computer wins!")
elif choice == 0 and computer_choice == 2:
    print("Rock beats scissors, you win!")

elif choice == 1 and computer_choice == 0:
    print("Paper beats rock, you win!")
elif choice == 1 and computer_choice == 1:
    print("It's a draw!")
elif choice == 1 and computer_choice == 2:
    print("Scissors beats paper, Computer wins!")

elif choice == 2 and computer_choice == 0:
    print("Rock beats scissors, computer wins!")
elif choice == 2 and computer_choice == 1:
    print("Scissors beats paper, you win!")
elif choice == 2 and computer_choice == 2:
    print("It's a draw!")

