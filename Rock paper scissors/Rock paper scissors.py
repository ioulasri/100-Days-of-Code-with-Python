import random

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
user_choice = input("Choose 'r' for rock, 'p' for paper or 's' for scissors\n").lower()

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    computer_choice = rock
if computer_choice == 1:
    computer_choice = paper
if computer_choice == 2:
    computer_choice = scissors
if user_choice == "s":
    user_choice = scissors
if user_choice == "p":
    user_choice = paper
if user_choice == "r":
    user_choice = rock

if user_choice != rock and user_choice != paper and user_choice != scissors:
    print("Invalid choice!!")
    quit()
else:
    if user_choice == rock and computer_choice == paper or user_choice == paper and computer_choice == scissors or \
            user_choice == scissors and computer_choice == rock:
        print("Computer choice is:\n" + computer_choice + "\nYour choice was: \n" + user_choice)
        print("You lost!!")

    elif user_choice == paper and computer_choice == rock or user_choice == scissors and computer_choice == paper \
            or user_choice == rock and computer_choice == scissors:
        print("Computer choice is:\n" + computer_choice + "\nYour choice was: \n" + user_choice)
        print("You Won!!")

    else:
        print("Computer choice is:\n" + computer_choice + "\nYour choice was: \n" + user_choice)
        print("Draw!!")


