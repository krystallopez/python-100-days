print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# Conditional statements in Python
# if height >= 120:
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# (Comparison Operators)
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to

# Nested if and elif statements
# if height >= 120:
#   print("You can ride the rollercoaster")
#   age = int(input("how old are you?"))
#   if age < 12:
#     print("Please pay $5")
#   elif age <= 18:
#     print("Please pay $7")
#   else:
#     print("Please pay $12")
# else:
#   print("Sorry, you have to grow taller before you can ride.")


# Multiple if Statements in succession
# if height >= 120:
#   print("You can ride the rollercoaster")
#   age = int(input("how old are you?"))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7")
#   else:
#     bill = 12
#     print("Adult tickets are  $12")

#   wants_photo = input("Do you want a photo taken? Y or N.\n")
#   if wants_photo == "Y":
#     bill += 3

#   print(f"Your final bill is: ${bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride.")


# Logical Operators
# and => when you combine two different conditions with the and operator they both have to be true for the entire line of code to be True. If just one of them is true, the code will evaluate to False

# or => If only one condition is True, then it will be evaluated to True, or if conditions are both True it will evaluate to True. This only becomes false when both conditions are evaluated to be False.

# not => All this does is it basically reverses a condition, if the condition is False then it becomes True and if the condition is True then it becomes False

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("how old are you?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay have a free ride on us")
    else:
        bill = 12
        print("Adult tickets are  $12")

    wants_photo = input("Do you want a photo taken? Y or N.\n")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
