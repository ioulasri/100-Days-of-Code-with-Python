import random
import art, data
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


current_score = 0
print(art.logo)
print("\n\nWelcome to higher or lower 🤗")

while True:
    print(f"Your current score is: {current_score}")
    a = random.choice(data.data)
    b = random.choice(data.data)
    while a == b:
        b = random.choice(data.data)
    res = int(a["follower_count"]) - int(b["follower_count"])
    print("A : " + a["name"] + ", " + a["description"] + ",from " + a["country"] + "\n")
    print(art.vs + "\n")
    print("B : " + b["name"] + ", " + b["description"] + ",from " + b["country"])
    print("\nWho has more followers?")
    compare = input("press 1 for A or 2 for B:\n")
    clear_screen()
    print(art.logo)
    if compare == "1":
        if res > 0:
            print("That's correct 😎")
            current_score += 1
        else:
            print("That's wrong 😓")
            print(f"Final score is: {current_score}")
            quit()
    if compare == "2":
        if res < 0:
            print("That's correct 😎")
            current_score += 1
        else:
            print("That's wrong 😓")
            print(f"Your score is: {current_score}")
            quit()
