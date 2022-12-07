import random
# Write a program that will randomly pick the name of person that will pay the bill, you cannot use the choice function

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")


# Write your code below this line 👇
# This was my solution
# print(names)

# names_len = len(names)
# print(names_len)
# print(f"The length of this list is: {names_len}")

# names_ran = random.randint(0,4)
# bill_pay = names[names_ran]

# print(f"{bill_pay} is going to buy the meal today!")

# Solution

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names) # prints the length of the list, total number of items in the list

random_choice = random.randint(0, num_items - 1) # This will give us a random number between 0 and the length of the number of items in the list, we use num_items - 1 because we want one less then the length of the list as the computer reads the number of items in the list from 0 to 4

print(random_choice) # This will print the random number, and will allow us to generate a random number from 0 to the last index and we can store in the variable random_choice

pay_person = names[random_choice] # This will correspond with the index of the list, random_choice will be a number and that number will then be the index that we reference making this now names[1] which would print "Krystal". We can store this value in the variable pay_person. We can then use an f string to include that variable and  print out our expected output below:


print(f"{pay_person} is going to buy the meal today!")


# You can also use the choice() function and get the same outcome by writing the code as follows:
# pay_person = random.choice(names)
# print(pay_person + "is going to buy the meal today!")

