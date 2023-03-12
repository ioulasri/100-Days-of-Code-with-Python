import random  # For number generation
import re  # For regular expression functionality

# Game setup
print("Welcome to Hangman!")
print("There are multiple difficulty settings shown below:")
print("\t1. Beginner (10 lives)")
print("\t2. Intermediate (8 lives)")
print("\t3. Expert (6 lives)")
print("\t4. Advanced (4 lives)")
print("\t5. Insane (2 lives)")

# Choose a difficulty level
user_setting = input("Please choose a difficulty by typing its number: ")

# Establish a list of words that can be chosen for the game

word_list = ["imad", "eat", "cry"]


# Inform the user of their selection
if user_setting == "1":
    number_of_lives = 10
    print("\nYou have chosen %s and will receive %d lives." % ("Beginner", number_of_lives))
elif str(user_setting) == "2":
    number_of_lives = 8
    print("\nYou have chosen %s and will receive %d lives." % ("Intermediate", number_of_lives))
elif str(user_setting) == "3":
    number_of_lives = 6
    print("\nYou have chosen %s and will receive %d lives." % ("Expert", number_of_lives))
elif str(user_setting) == "4":
    number_of_lives = 4
    print("\nYou have chosen %s and will receive %d lives." % ("Advanced", number_of_lives))
elif str(user_setting) == "5":
    number_of_lives = 2
    print("\nYou have chosen %s and will receive %d lives." % ("Insane", number_of_lives))
else:
    number_of_lives = 10
    print("\nYou have made an invalid selection and will receive %d lives by default." % number_of_lives)

# Pick a random word from the list
random_num = random.randint(0, len(word_list) - 1)
word_chosen = word_list[random_num]

# Encode the word with dashes
encoded_word = re.sub('[0-9a-zA-Z]', '-', word_chosen)


# Define a function for handling guesses
def guess(letter, word, encoded):
    # Does the letter exist within the word?
    found = False
    if letter in word:
        found = True
        # Replace the dashes with the letter
        for i in range(0, len(word)):
            if word[i] == letter:
                encoded = encoded[0:i] + letter + encoded[i + 1:len(encoded)]
    return found, encoded


# Initiate the game and prompt the user for their first selection
print("\nTime to guess a letter! You have %d lives remaining." % number_of_lives)
print(encoded_word)

while number_of_lives > 0:
    guessed_letter = input("Your guess: ")[:1]

    letter_found, encoded_word = guess(guessed_letter, word_chosen, encoded_word)

    if not letter_found:
        number_of_lives -= 1
        if number_of_lives == 0:
            print("\nGame over, you lost! :( The word or phrase was '%s'" % word_chosen)
            break
        else:
            print("\nWhoops! That letter was not found. You now have %d lives remaining." % number_of_lives)
            print(encoded_word)
    else:
        if "-" not in encoded_word:
            print("\nHooray! You won with %d lives remaining. The word or phrase was '%s'" % (
                number_of_lives, word_chosen))
            break
        else:
            print("\nGood job! That letter was found. You still have %d lives remaining." % number_of_lives)
            print(encoded_word)
