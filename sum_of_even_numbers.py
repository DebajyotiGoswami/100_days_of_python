#Write your code below this row 👇

even_sum = 0

# for each_num in range(1 , 101):
#     if each_num % 2 == 0:
#         even_sum += each_num

for each_even in range(2 , 101 , 2):
    even_sum += each_even
    
print(f"Sum of all even numbers is {even_sum}")
