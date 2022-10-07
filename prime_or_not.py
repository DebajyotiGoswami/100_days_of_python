number = int(input("what is the number ? "))

for i in range(2 , number // 2):
    if number % i == 0:
        print(f"{number} is not a prime number")
        break

if i == number //2 :
    print(f"{number} is a prime number")
