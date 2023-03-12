import random

from hangman import words

print(words.logo)
displayed_word = []
end_game = False
word = random.choice(words.words)
word_lenght = len(word)
lives = 6
letter = ""
#print(f"psst this is the word: {word}")
guessed_words = []

for i in word:
    displayed_word.append("_")

while not end_game and lives >= 0:
    guess = input("Enter a guess: ").lower()
    for position in range(word_lenght):
        letter = word[position]
        if letter == guess:
            displayed_word[position] = letter
    print("".join(displayed_word))
    if guess not in word:
        print(f"{guess} is not in the word")
        if guess in guessed_words:
            print(f"You've already guessed {guess}")
        guessed_words.append(guess)
        print(words.stages[lives])
        lives -= 1
        print(f"you have {lives + 1} lives more!")

    if "_" not in displayed_word:
        print("You win")
        end_game = True
