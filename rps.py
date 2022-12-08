# First we need to import randint from the random module, this is how the computer opponent will play
from random import randint
print("Let's play rock, paper, scissors!")
print("""
Rock 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)


Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Then we create list of play options
items = ["Rock", "Paper", "Scissors"]

# next we set up our players, the computer and you

# We need to assign a random play to the computer
computer = items[randint(0, 2)]


# We assign a random play to the computer using our list and the randint functin. Why did we choose (0,2)? We have to remember that computers start counting at 0, so 0 is "Rock", 1 is "Paper", and 2 is "Scissors". This will allow the computer to pick from one of the indexes in the items list.

# create a variable for player and set it to false
player = False

# Why did we set the player to False? Basically once the while loop starts the computer will wait for you to make a play , your status will then change from False to True once you have taken your turn.

while player == False:
    # here we will set the player to true
    player = input("Rock, Paper, Scissors\n")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print(f"You lose!, {computer}, covers, {player}")
        else:
            print(f"You win!, {player}, smashes, {computer}")
    elif player == "Paper":
        if computer == "Scissors":
            print(f"You lose!, {computer}, cut, {player}")
        else:
            print(f"You win!, {player}, covers, {computer}")
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You lose!, {computer}, smashes, {player}")
        else:
            print(f"You win!, {player}, cut, {computer}")
    else:
        print("This is not a valid play. Check your spelling!")

    player = False
    computer = items[randint(0, 2)]


#  We use nested if/elif/else statements to check every possible outcome of the game and return a message stating the winner, a tie, or an error. We use else at the end to catch anything that isn't rock, paper, or scissors. Then we reset the player to false so that we can restart the while loop.
