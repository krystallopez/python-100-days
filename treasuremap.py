# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 

# The first digit in the input will specify the column (the position on the horizontal axis).

# The second digit in the input will specify the row number (the position on the vertical axis). 

# Things to remember: 
# 1. First, your program must take the user input and convert it to a usable format
# 2. Next, you need to use that input to update your nested list with an "x". Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].

# column 2, row 3 would be entered as:

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']


row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0])
row = int(position[1])

map[row - 1][column - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")