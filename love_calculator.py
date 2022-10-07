# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sum1 , sum2 = 0 , 0
both_names = (name1 + name2).lower()
for letter in "true":
    sum1 += both_names.count(letter)
for letter in "love":
    sum2 += both_names.count(letter)
    
love_score = int(str(sum1) + str(sum2))

if love_score < 10 or love_score > 90:
    message = "You go together like coke and mentos"
elif love_score < 50 and love_score > 40:
    message = "You are alright together"
else:
    message = "thats all"

print(f"Your score is {love_score} and {message}")


