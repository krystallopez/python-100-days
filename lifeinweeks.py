#Create a program using maths and f-String that tells us how many days, weelks, months, we have left if we live until 90 years old

# Takes user input for their current age 
age = input("What is your current age? ")

# I created a variable called new_age that would be equal to the age variable after its converted to an integer. I printed the n

new_age = int(age)

# created a new variable called old_age that holds the value of 90 - new_age, I used this as my basis for the following calculations 

old_age = 90 - new_age

# old_age is equal to 58, so I use the value of 58 and multiply by 365 to calculate how many days until I am 90

days = old_age * 365

# old_age is equal to 58, so I use the value of 58 and multiply by 52 to calculate how many weeks until I am 90

weeks = old_age * 52

#old_age is equal to 58, so I use the value of 58 and multiply by 12 to calculate how many months until I am 90

months = old_age * 12

#using an f-String, I combined all of the data values and printed out a message that shows how much time I have left until I am 90


message = f"You have {days} days, {weeks} weeks, and {months} months left"

print(message)







