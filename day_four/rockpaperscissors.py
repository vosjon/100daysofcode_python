# Day 4 of 100 - Rock, Paper, Scissors
import random as r

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

print("Let's play rock, paper, scissors!")
player_choice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

computer_choice = r.randint(1, 3)
print("\nYou chose:\n")
if player_choice == 1:
    print(rock)
elif player_choice == 2:
    print(paper)
else:
    print(scissors)

print("\nThe computer got:\n")
if computer_choice == 1:
    print(rock)
elif computer_choice == 2:
    print(paper)
else:
    print(scissors)

print()
if player_choice == computer_choice:
    print("It's a draw.")
elif player_choice == 1 and computer_choice == 3: # Player Rock, computer scissors
    print("Rock beats scissors. You win!")
elif player_choice == 3 and computer_choice == 2: # Player scissors, computer paper
    print("Scissors beats paper. You win!")
elif player_choice == 2 and computer_choice == 1: # Player paper, computer rock
    print("Paper beats rock. You win!")
elif computer_choice == 1 and player_choice == 3: # Computer Rock, player scissors
    print("Rock beats scissors. You lose!")
elif computer_choice == 3 and player_choice == 2: # Computer scissors, player paper
    print("Scissors beats paper. You lose!")
elif computer_choice == 2 and player_choice == 1: # Computer paper, player rock
    print("Paper beats rock. You lose!")
