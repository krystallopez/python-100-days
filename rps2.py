import random

print("Let's play a game of: \n")

rock = ''' Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(rock)
print(paper)
print(scissors)

# Write your code below this line 👇

choices = [rock, paper, scissors]

player_pick = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(choices[player_pick])

comp_pick = random.randint(0, 2)
print("Computer pick was: ")
print(choices[comp_pick])

if player_pick >= 3 or player_pick < 0:
    print("That is an invalid choice. Please choose a number between 0 and 3")
elif player_pick == 0 and comp_pick == 2:
    print("Rock smashes scissors, you win!")
elif comp_pick == 0 and player_pick == 2:
    print("Rock smashes scissors, you lose!")
elif comp_pick > player_pick:
    print("You lose, the computer beat you!")
elif player_pick > comp_pick:
    print("You win, the computer is a loser!")
elif comp_pick == player_pick:
    print("It's a tie!")
