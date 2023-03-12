import random
import art
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def append_card(a):
    random_card = random.choice(cards)
    a.append(random_card)

def playing():
    user_cards = []
    computer_cards = []
    sum_own = 0
    sum_com = 0
    print(art.logo)

    welcome = "Welcome to blackjack!!"
    print(welcome)
    append_card(user_cards)
    append_card(user_cards)
    append_card(computer_cards)
    append_card(computer_cards)
    preview_own = "    Your cards are: " + str(user_cards) + ",Current score: " + str(sum(user_cards)) 
    preview_com = "    The first computer card is: " + str(computer_cards[0])
    print(preview_own)
    print(preview_com)

    hit_or_set = input("To hit press 'h' , To set press 's': \n")
    if hit_or_set == 'h':
        check(sum_own, sum_com, user_cards, computer_cards)
        print("Your cards were: " + str(user_cards) + " - Total score: " + str(sum(user_cards)))
        print("Computer cards were :" + str(computer_cards) + " - Total score: " + str(sum(computer_cards)))
    if hit_or_set == 's':
        append_card(user_cards)
        check(sum_own, sum_com, user_cards, computer_cards)
        print("Your cards were: " + str(user_cards) + " - Total score: " + str(sum(user_cards)))
        print("Computer cards were :" + str(computer_cards) + " - Total score: " + str(sum(computer_cards)))
    play = input("To play again press 'p' to leave press 'n':\n").lower()
    if play == "p":
        clear_screen()
        playing()

    else:
        print("Bye")
        quit()
    again = input("To hit press 'h' , To set press 's': \n")
    if again == 'h':
        check(sum_own, sum_com, user_cards, computer_cards)
        print("Your cards were: " + str(user_cards) + " - Total score: " + str(sum(user_cards)))
        print("Computer cards were :" + str(computer_cards) + " - Total score: " + str(sum(computer_cards)))
    if again == 's':
        append_card(user_cards)
        check(sum_own, sum_com, user_cards, computer_cards)
        print("Your cards were: " + str(user_cards) + " - Total score: " + str(sum(user_cards)))
        print("Computer cards were :" + str(computer_cards) + " - Total score: " +str(sum(computer_cards)))
    play = input("To play again press 'p' to leave press 'n':\n").lower()
    if play == "p":
        clear_screen()
        playing()

    else:
        print("Bye")
        quit()


def check(a, b, c, d):
    for i in c:
        a += i
    for n in d:
        b += n
    if b < 17:
        append_card(d)
        b += d[2]
    if b < 17:
        append_card(d)
        b += d[3]
    if a > 21:
        print("The total of your cards is over 21..\nYou lost!!😤")
    elif b > 21:
        print("The total of computer cards is over 21..\nYou won!!😎")
    elif a > b:
        print(f"The total of your cards is {a} and the total of computer cards is {b}\nYOU WON!!😎")
    elif b == a:
        print(f"The total of your cards is {a} and the total of computer cards is {b}\nYOU DRAW!!🙃")
    else:
        print(f"The total of your cards is {a} and the total of computer cards is {b}\nYOU LOST!!😤")


playing()
