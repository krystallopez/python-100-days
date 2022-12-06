print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

direction = input(
    "You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if direction == "left":
    boat_or_swim = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across").lower()
    if boat_or_swim == "wait":
        color = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red,     one yellow, and one blue. which color do you choose? ").lower()
        if color == "red":
          print("YOU LOSE!")
        elif color == "yellow":
            print("You did it! You found the treasure you win!")
        elif color == "blue":
          print("You lost!")
        else:
            print("Sorry, game over. You walked into a room full of beasts.")
    else:
        print("Sorry, game over! You drowned from swin=mming in deep water.")
else:
    print("Sorry. Game Over. You walked into a pit of snakes")

# direction = input(
#     "You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")

# if direction == "left":
#     wait_or_swim = input(
#         "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim accross.\n").lower()
#     if wait_or_swim == "wait":
#         color = input(
#             "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. which color do you choose? \n").lower()
#         if color == "red":
#             print("Sorry, game over. You walked into a room full of black widows")
#         elif color == "yellow":
#             print("You've done it! You found the treasure you win!")
#         elif color == "blue":
#             print("Oof. GAME OVER! You went into a room full of hungry lions")
#         else:
#             print("That door doesn't exist, pick either, red, yellow, or blue.")
# else:
#     print("Sorry, kid. You fell into a pit of snakes. Better luck next time.")
