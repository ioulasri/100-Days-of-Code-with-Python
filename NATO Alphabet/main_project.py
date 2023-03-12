import pandas

our_data = pandas.read_csv("data.csv")

letters = our_data["letter"].tolist()
words = our_data["words"].tolist()
dictionary = {}
for i in range(len(letters)):
    dictionary[letters[i]] = words[i]

name = input("Enter your name: ")
name_letter = [i for i in name]
nato = []
for i in name_letter:
    try:
        nato.append(dictionary[i.upper()].strip())
    except:
        pass
print(nato)