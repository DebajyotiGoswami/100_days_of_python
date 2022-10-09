#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲


import random

# for _ in range(10):
#     random_int = random.randint(1 , 2)
#     if random_int == 1:
#         print("HEAD")
#     elif random_int == 2:
#         print("TAIL")
#     else:
#         print("ERROR")

# list_of_choices = ['HEAD' , 'TAIL']
# for _ in range(10):
#     print(random.choice(list_of_choices))


list_of_choices = ["HEAD" , "TAIL"]
list_of_results = [random.choice(list_of_choices) for _ in range(10)]
print(list_of_results)
print(list_of_results.count("HEAD") , list_of_results.count("TAIL"))



