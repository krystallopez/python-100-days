# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
both_names = name1 + name2 # combines the two words together so that we can check for each letter
lower_names = both_names.lower() # changes them to lower case so that all of the letters can be counted

t = lower_names.count("t") #counts how many times t occurs in the combined string
r = lower_names.count("r") #counts how many times r occurs in the combined string
u = lower_names.count("u") #counts how many times u occurs in the combined string
e = lower_names.count("e") #counts how many times e occurs in the combined string

first_score = t + r + u + e # adds all of the values together

l = lower_names.count("l") #counts how many times l occurs in the combined string
o = lower_names.count("o") #counts how many times o occurs in the combined string
v = lower_names.count("v") #counts how many times v occurs in the combined string
e = lower_names.count("e") #counts how many times e occurs in the combined string

second_score = l + o + v + e # adds all of the values together


final_score = int(str(first_score) + str(second_score)) #we want to be able to concatenate them together so we can add them together, ex: "7" + "3" = "73". Even though we converted the number to strings, we need to convert the now concantenated string into an integer so that our condition can be evaluated as True or False. 

# If we do not do this, we will get a TypeError, because in order to concatenate the numbers we had to convert them into strings, we want to compare the final_score to an actual number, so in order to do that, we then need to convert the string back to an integer.


# using logical operators to check if the conditions are True or False
if (final_score < 10) or (final_score > 90):
    print(f"Your score is {final_score}, you go together like coke and mentos.")
    # only one of these items needs to be evaluated as True in order for the statement to print
elif (final_score >= 40) and (final_score <= 50):
    print(f"Your score is {final_score}, you are alright together.")
    # both of these conditions need to be true in order for this statement to print 
else:
    print(f"Your score is {final_score}")
    # if the score does not match any of the conditions listed, then this line will print.