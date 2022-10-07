# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            remark = "a leap year"
        else:
            remark = "not a leap year"
    else:
        remark = "a leap year"
else:
    remark = "not a leap year"

print(f"the year {year} is {remark}")
