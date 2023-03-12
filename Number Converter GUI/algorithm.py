import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def _ToDec(num):
    numb = int(input("Enter your binary number:\n"))
    e = 0
    deci = []
    result = []
    for index in str(numb):
        deci.append(index)
    deci.reverse()
    for index in deci:
        z = num ** e
        f = z * int(index)
        result.append(f)
        e += 1
    return sum(result)


def hexas():
    hexadecimal = input("Enter your hexadecimal number:\n")
    result = []
    e = 0
    num = []
    h = []
    for index in hexadecimal:
        num.append(index)
    num.reverse()
    for index in num:
        if index == "A":
            h.append(10)
        elif index == "B":
            h.append(11)
        elif index == "C":
            h.append(12)
        elif index == "D":
            h.append(13)
        elif index == "E":
            h.append(14)
        elif index == "F":
            h.append(15)
        else:
            h.append(index)
    for index in h:
        w = 16 ** e
        f = w * int(index)
        result.append(f)
        e += 1
    return sum(result)


working = True
while working:
    first = input("\n\nWhat do you want to convert:\n1- Decimal number\n2- Binary number\n3- Hexadecimal number:\n")
    if first == 'q':
        print('Turning off..')
        quit()
    second = input("\n\nTo what do you want to convert:\n1- Decimal number\n2- Binary number\n3- Hexadecimal number:\n")
    if second == 'q':
        print('Turning off..')
        quit()
    clear_screen()
    if first == "1":
        if second == "1":
            dec = input("Enter your decimal number:\n")
            print("Your decimal number is:\n" + dec)
        elif second == "2":
            number = int(input("Enter your decimal number:\n"))
            if number == 0:
                print("0000")
            binary_numbers = []
            while number > 0:
                a = number % 2
                binary_numbers.append(a)
                number = number // 2
            binary_numbers.reverse()
            print("Your binary number is:")
            for i in binary_numbers:
                print(i, end="")
        elif second == "3":
            number = int(input("Enter your decimal number:\n"))
            binary_numbers = []
            while number > 0:
                a = number % 16
                if a == 10:
                    a = "A"
                if a == 11:
                    a = "B"
                if a == 12:
                    a = "C"
                if a == 13:
                    a = "D"
                if a == 14:
                    a = "E"
                if a == 15:
                    a = "F"
                binary_numbers.append(a)
                number = number // 16
            binary_numbers.reverse()
            print("Your hexadecimal number is:")
            for i in binary_numbers:
                print(i, end="")

    if first == "2":
        if second == "1":
            print("Your Decimal number is: " + str(_ToDec(2)))
        elif second == "2":
            binary = input("Enter your binary number:\n")
            print("Your binary number is:\n" + binary)
        elif second == "3":
            b = _ToDec(2)
            binary_numbers = []
            while b > 0:
                a = b % 16
                if a == 10:
                    a = "A"
                if a == 11:
                    a = "B"
                if a == 12:
                    a = "C"
                if a == 13:
                    a = "D"
                if a == 14:
                    a = "E"
                if a == 15:
                    a = "F"
                binary_numbers.append(a)
                b = b // 16
            binary_numbers.reverse()
            print("Your hexadecimal number is:")
            for i in binary_numbers:
                print(i, end="")

    if first == "3":
        if second == "1":
            print("Your decimal number is: " + str(hexas()))
        elif second == "2":
            binary_numbers = []
            t = hexas()
            while t > 0:
                a = t % 2
                binary_numbers.append(a)
                t = t // 2
            binary_numbers.reverse()
            print("Your binary number is:")
            for i in binary_numbers:
                print(i, end="")
        elif second == "3":
            dec = input("Enter your hexadecimal number:\n")
            print("Your hexadecimal number is:\n" + dec)
