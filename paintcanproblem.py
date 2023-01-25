# Write your code below this line 👇
# ---> This allows to import the math module so that you can use the math() function.
import math


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.
def paint_calc(height, width, cover):
    # ----> This will calcute the number of cans needed, height will hold the value of the height of the wall, width will hold the value of the width of the wall, cover will hold the value of how much coverage is needed and has already been set on line 15.
    num_cans = (height * width) / cover
    # ---> math.ceil will round the number up to the number's nearest integer
    round_up_cans = math.ceil(num_cans)
    # ---> This line prints out an f-string that will include the number of cans needed
    print(f"You'll need {round_up_cans} cans of paint")


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
