height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Write your code below this line 👇
int_weight = int(weight)
float_height = float(height)

bmi = int_weight/float_height ** 2
int_bim = int(bmi)

print(int_bim)