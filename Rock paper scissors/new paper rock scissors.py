

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
computer_choice = ""

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
    if user_choice == rock:
        computer_choice = paper
    elif user_choice == paper:
        computer_choice = scissors
    elif user_choice == scissors:
        computer_choice = rock

print("Computer choice: \n" + computer_choice + "\nYour choice: \n" + user_choice)
print("You lost")