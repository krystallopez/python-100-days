student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# print(len(student_heights))
sum = 0

for height in student_heights:
    sum += height
# print(f"total height = {sum}")

student_number = 0
for student in student_heights:
    student_number += 1
# print(f"number of students = {student_number}")

average = round(sum/student_number)
print(average)
