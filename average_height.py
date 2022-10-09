# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# sum_of_heights = sum(student_heights)
# count_of_heights = len(student_heights)

# avg_of_heights = sum_of_heights / count_of_heights

sum_of_heights , count_of_heights = 0 , 0
for each_height in student_heights:
    count_of_heights += 1
    sum_of_heights += each_height

avg_of_heights = sum_of_heights / count_of_heights
print(f"Average of {count_of_heights} nos students is {avg_of_heights}")



