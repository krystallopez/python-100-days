#Data Types in Python 

print(len("bananas")) 
#gets the number of items in a container or a string

#Strings- a string of characters

"hello" 
#Strings need to be created with double quotes arouund them

print("Hello"[4]) 
#Prints out the first character of the string, which would be at the index of 0, this is called Subscripting!

#Integer- numbers without any decimal places

print(123 + 345)
#integers need to be written without double quotes

print(123_456)
#Use the underscore to act as a comma to separate the numbers, the computer will read it as 123,456. If you use a comma it will create between the numbers

#Float- a number with a decimal point 

print(3.14159)

#Boolean- only has two values, and start with a capital letter 

True 
False

#This will determine if something in your program is either truthy or falsy

#Type Error
# num_char = len(input("what is your name?"))
# print("Your name has " + num_char + " characters.")
#You will receive a Type Error due to the fact an integer cannot be concatenated to a string, only strings can be concantenated.

# print(type(num_char)) #type tells you the data type of the input that is received

#Type Conversion/Type Casting

# new_num_char = str(num_char) #str converts an integer to a string 
# print(new_num_char)
# print("Your name has " + new_num_char + " characters.")

a = int("123") # float will convert a number to a floating point number
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

#Mathematical operations in Python
# + = addition 
# - = subtraction
# * = multiplication
# / = division
# ** = exponents, or when you want to raise a number to a power

print(6/3) 
# When you divide two numbers, you will always receive a floating point number, this is just something that happens in python 

# ** = exponents, or when you want to raise a number to a power
print(2 ** 3)

# Python follows the rules of PEMDAS, following the order of operations 

# PEMDAS
# () => Parentheses
# ** => Exponent
# * => Multiplication
# / => Division 
# + => Addition 
# - => Subtraction

print(3 * (3 + 3) / 3 - 3)

# Number Manipulation and F strings in Python

print(round(8/3))
# round function will round up to the nearest whole number, you can also specify the precision that you want the number rounded to 

print(round(8 / 3, 2)) # adding the 2 after the division will round it to two decimals places

print( 8 // 3) # This is floor division, this will return the answer as an integer rather than a floating point number

result = 4 / 2
result /= 2 # this divides the result by 2 again
print(result)

# Adding a point to a score 
score = 0 
score += 1
print(score)

# F strings- allows you to type the character f in front of a string and it then becomes an F string which allows you add various values into a print function. This eliminates having to convert every single data type you want included in the string

points = 0
height = 1.8
isWinning = True

print(f"your score is: {points}, your height is: {height}, and you are winning is {isWinning}")


