# Adding even numbers using the range function and a for loop

# 1. Start with a counter, or an accumulator so that you have a base to start with. Remember the computer starts counting from 0. So we will represent the total using the variable total as show below:

total = 0

# 2. Now that we have an accumulator, we can then start to construct our for loop as seen below:

for number in range(2, 101, 2):
    total += number
print(total)

# 3. The problem is asking that we add all even numbers, so we have to set the range to account for all the even numbers, notice that we start off from 2, and set the step to 2, this will give us the range that includes all of the even numbers up to 100.

# 4. Then we add the number to the current total and outside the for loop we can print what the total amount will be

# Here is another solution that we can do and this will help with the fizzbuzz problem as well

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)
