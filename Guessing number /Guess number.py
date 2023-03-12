import random
import art
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print(art.logo)
print("Welcome to the guessing number game!!")
difficulty = input("Please choose a difficulty:\n-'h' for hard (5 attempts)\n-'e' for easy (10 attempts):\n").lower()

if difficulty == 'h':
    hard = 5
    print("Okay you chosen the hard way to play this game..")
    seil_number = int(input("Enter a number to guess from zero to..:\n"))
    number = random.randint(1, seil_number)
    while hard != 0:
        guess = int(input(f"Enter a guess between 0 and {seil_number}\n-"))
        if guess > seil_number:
            hard -= 1
            print(f"You went over the seiling number\nyou have {hard} more attempts..")
        if guess > number:
            hard -= 1
            print(f"Too high!!\nyou have {hard} more attempts..")
        if guess < number:
            hard -= 1
            print(f"Too low!!\nyou have {hard} more attempts..")
        if guess == number:
            print(f"You guessed {number} correctly and won with {hard} more attempts left!!")
    if hard == 0:
        print(f"You lost.. the number was {number}")
if difficulty == 'e':
    easy = 10
    print("Okay you chosen the hard way to play this game..")
    seil_number = int(input("Enter a number to guess from zero to..:\n"))
    number = random.randint(0, seil_number)
    while easy != 0:
        guess = int(input(f"Enter a guess between 0 and {seil_number}\n-"))
        if guess > seil_number:
            easy -= 1
            print(f"You went over the seiling number\nyou have {easy} more attempts..")
        if guess > number:
            easy -= 1
            print(f"Too high!!\nyou have {easy} more attempts..")
        if guess < number:
            easy -= 1
            print(f"Too low!!\nyou have {easy} more attempts..")
        if guess == number:
            print(f"You guessed {number} correctly and won with {easy} more attempts left!!")
    if easy == 0:
        print(f"You lost.. the number was {number}")
