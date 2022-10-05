##calculate the remaining weeks in your life

age = int(input("Enter your age in years : "))
years_remaining = 90 - age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52

message = f"You have {years_remaining} years , {months_remaining} months , {weeks_remaining} weeks remaining in your life"
print(message)
