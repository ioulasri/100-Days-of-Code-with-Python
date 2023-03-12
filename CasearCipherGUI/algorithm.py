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
    return word


def decrypt(my_text, my_shift):
    for i in range(len(my_text)):
        letter = my_text[i]
        if letter in alphabet:
            new_letteer = alphabet[alphabet.index(letter) - my_shift]
            new_text.append(new_letteer)
        else:
            new_text.append(letter)

    word = "".join(new_text)
    return word


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
new_letter = ""
new_text = []
