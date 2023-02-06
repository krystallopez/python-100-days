def prime_checker(number):
  is_Prime = True
  for i in range(2, number):
    if number % i == 0:
      is_Prime = False
  if is_Prime:
    print("It is a prime number")
  else: 
   print("It's not a prime number") 


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# The functions checks whether or not the number that you are passing in is a prime number. 

# 1. We create the function, called prime_checker and we pass in an argument an argument called number to the parameter

# 2.  we need to figure out how we can determine whether or not the number is a prime. For this we can use the modulus operator to check whether the numbe that we are passing in can be divided by all the numbers all the way down to 2. (See line 9)

# 3. We can use a for loop to go through the process of dividing the number by numbers starting from two. We create a for loop and say for i, which is going to be number that we are going to divide by (i, is for iteration of the loop, starting from 2 to the number that is passed is as the argument). We start the range from two because we know all numbers are divisible by 1.

# 4. The range starts from 2 because we are not going to divide by 1. We are going to put the range all the up to the number. In the for loop, we can start to do our divisions. We can take the number and use the modulo operator to divide it by i.

# 5. This will make it so it's exactly the same for each line of division. If the number divided by i is zero is equal to 0 then it is not a prime number. If that number can be divided  by any of the numbers between 2 and number - 1 cleanly with no remainder, then that means it is not a prime number. 

# 6. We can create a variable call isPrime and set it to True. If this is statement gets triggered then we switch this isPrime to False. When we get to the end of the for loop we can check to see if isPrime True or is it False. If isPrime is True then that code block will be triggered and the print statement will then be shown in the console once the code black is run.  Else, then we are going to print the opposite stating that the number is not a prime number.

 

