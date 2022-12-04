#solve the two digit number problem 
two_digit_number = input("enter a two digit number\n")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

sum = first_digit + second_digit

str_sum = str(sum)

print("The sum of the two digit number is: " + str_sum)
