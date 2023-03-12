# TODO: Create a letter using starting_letter.txt
with open("../Letter/Input/Letters/starting_letter.txt", mode="r") as file:
    a = file.read()


with open("../Letter/Input/Names/invited_names.txt") as f:
    line = f.readlines()
for name in line:
    n = name.strip()
    with open(f"../Letter/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        new = a.replace("[name]", n)
        print(new)
        file.write(new)


