a = 0
for i in range(1, 11):
    a += 1
    print()
    for j in range(1, 6):
        if j*a < 10:
            print(f"{j*a}", end='    ')
        else:
            print(f"{j*a}", end='   ')
