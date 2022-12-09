for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:  
    print("Fizzbuzz")
  elif number % 3 == 0: 
    print("Fizz")
  elif number % 5 == 0 :
    print("Buzz")
  else: 
    print(number)


# 1. Line 2 checks if the number is divisible by 3 and 5, if so computer will print "Fizzbuzz". however this line needs to be listed as we know that with if/elig/else statements will stop once it's found one statement that is true 

# 2. We want to first check if it is divisible by 3 and by 5 and then check to see if its divisble by 3, and then proceed to check if it is divisble by 5. If none of the statements are true, then we can just print the number. 