import art

print(art.logo)


def encrypt(my_text, my_shift):
    for i in range(len(my_text)):
        letter = my_text[i]
        if letter in alphabet:
            if alphabet.index(letter) + my_shift < len(alphabet):
                new_letteer = alphabet[alphabet.index(letter) + my_shift]
                new_text.append(new_letteer)
            else:
                new_letteer = alphabet[(alphabet.index(letter) + my_shift) - len(alphabet)]
                new_text.append(new_letteer)
        else:
            new_text.append(letter)

    word = "".join(new_text)
    print(word)


def decrypt(my_text, my_shift):
    for i in range(len(my_text)):
        letter = my_text[i]
        if letter in alphabet:
            new_letteer = alphabet[alphabet.index(letter) - my_shift]
            new_text.append(new_letteer)
        else:
            new_text.append(letter)

    word = "".join(new_text)
    print(word)


while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    new_letter = ""
    new_text = []
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'q' to leave at anytime:\n")
    if direction == 'q':
        print('Bye')
        quit()
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    elif direction == "q":
        print("bye")
        quit()
    else:
        print("you wrote something else try again..")
