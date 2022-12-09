# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
highest_score = 0 # we are starting this off at 0 as a counter, similar to index = 0
for score in student_scores: # loops through each score in the list 
    if score > highest_score: # checks to see if the current score is greater than the highest_score
        highest_score = score # if the score is greater than the highest score, then the score becomes the new value of the highest score
print(f"The highest score in the class is: {highest_score}")
