rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

weapons = [rock , paper , scissors]
possible_choices = ['rock' , 'paper' , 'scissors']
print("Welcome to Rock-Paper-Scissor game")

while True:    
    user_choice = input("Enter 'rock' or 'paper' or 'scissors'\n").strip().lower()
    if user_choice not in possible_choices:
        play_again = input("Wrong Choice. Want to play again ? Y /N ? ").lower()
        if play_again == 'y':
            continue
        else:
            break
    user_choice = possible_choices.index(user_choice)
    pc_choice = random.randint(0,2)
    print(f"User choose : \n{weapons[user_choice]}")
    print(f"Computer choose : \n{weapons[pc_choice]}")

    # if user_choice == pc_choice:
    #     print("It's a DRAW")
    # elif user_choice == 0:
    #     if pc_choice == 1:
    #         print("You LOOSE")
    #     else:
    #         print("You WIN")
    # elif user_choice == 1:
    #     if pc_choice == 0:
    #         print("You WIN")
    #     else:
    #         print("You LOOSE")
    # else:
    #     if pc_choice == 0:
    #         print("You LOOSE")
    #     else:
    #         print("You WIN")

    if user_choice == pc_choice:
        print("It's a DRAW")
    elif user_choice == 0 and pc_choice == 1:
        print("You LOOSE")
    elif user_choice == 1 and pc_choice == 2:
        print("You LOOSE")
    elif user_choice == 2 and pc_choice == 0:
        print("You LOOSE")
    else:
        print("You WIN")

    play_again = input("Wrong Choice. Want to play again ? Y /N ? ").lower()
    if play_again == 'y':
        continue
    else:
        break
