def guessing(guess, b, a):
    if int(guess) > a:
        return 1
    elif int(guess) < a:
        return 2
    elif int(guess) == a:
        return 3
    elif int(guess) > b:
        return 4
