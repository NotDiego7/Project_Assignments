# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(weight) / float(height) ** 2
BMI = str(BMI)
BMI_firstDigit = BMI[0]
BMI_secondDigit = BMI[1]
print(BMI_firstDigit+BMI_secondDigit)
