# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $")) #better to be set as float as the bill may not alwys be an even amount 

tip = int(input("What percentage tip would like to give? 10, 12, or 15? "))
#you may want to add something that lets the user know not to add the percent sign to the input as that would make it really to convert the 12% to an integer

people = int(input("How many people to split the bill? "))
#Converts the amount of people to an integer since it is taken in as a string


# Converting 12 to a decimal
tip_value = tip / 100

# Calcualting the tip amount
tip_amount = bill * tip_value

# calculating the total bill
total_bill = bill + tip_amount

# calculation pay per person
pay_per_person = total_bill / people

# rounding up to two decimal points using the round function 
final_bill = "{:.2f}".format(pay_per_person)

print(f"Each person should pay: {final_bill}")
