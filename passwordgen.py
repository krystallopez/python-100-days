#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""

# # This is the easy version of the exercise 
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)
#   # print(password)
  


# for sym in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
#   # print(password)

# for num in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
  
# print(f"Here is your password: {password}")



# 1. We can assume that nr_letters = 4, we are going to assume that the user only wants 4 letters to be stored in the password

# 2. we can add 1 to the range so that the range becomes 1-5 so that we can include 4. For every number in that range of 1-4 we are going to generate a random letter. We are going to pick out of the list of letters. To do we can generate a random number and use as the index, however we can also use the random.choice function as well. Inside the random.choice we can pass a sequence which in this case would be the letters list.

# 3. random_char = random.choice(letters), This will look through the letters list and generate a random letter. Make sure you are printing the random character in the for loop or else you will only get one number. We will need to add it to our password, which is why we assign it a variable. We can also simplify our code and just add the random.choice to the password. We can repeat the same process for the symbols and numbers as well. 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Now we do the hard version of this exercise, which will create more secure passwords and make it harder for hackers to try and get the password. 
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# In order to tackle the hard level of this problem, instead of adding everythng into the password variable we actually need to add into a list. Instead of using an empty string for the password variable, we will use a list. 

# To add thing to the list you can do the same thing as with the strings or we can use the append method for adding items to a list

# Now that we have a list, we have think about how we can shuffle through our list. We can either use a for loop or we can use an easier and cleaner way and use the random.shuffle() method. This will save us from having to create a new list. We can use that and then re-print the password list again.

# Now that we have the list created, we can use a for loop to loop through the password_list and add each indivdual character into the password variable. 

password_list = [] 

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for sym in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
for num in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))
  
# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Here is your password: {password}")
