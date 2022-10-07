# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height * height) , 2)
#print(bmi)

if bmi < 18.5:
    remark = "underweight"
elif bmi < 25:
    remark = "normal weight"
elif bmi < 30:
    remark = "overweight"
elif bmi < 35:
    remark = "obese"
else:
    remark = "clinically obese"

print(f"your bmi is {bmi} and you are {remark}")
