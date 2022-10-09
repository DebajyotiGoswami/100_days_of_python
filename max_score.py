# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = student_scores[0]

for each_score in student_scores:
    if each_score > max_score:
        max_score = each_score

print(f"Maximum score found is {max_score}")



    
