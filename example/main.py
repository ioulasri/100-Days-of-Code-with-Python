import math
def print_numbers(n):
    ranges = (2 * n) - 1
    RANGES = ranges
    list_n = []
    middle = math.floor(ranges / 2)
    for i in range(middle):
        list_n.append(n)
        n += 1
    for j in range(middle + 1):
        list_n.append(n)
        n -= 1
    for i in list_n:
        print(i, end="")

while True:
    rows = int(input("enter number of rows: "))
    if rows <0:
        quit()
    n = 1
    columns = rows
    while n < columns + n:
        for j in range(columns - 1):
            print(" ", end="")
        print_numbers(n)
        for j in range(columns - 1):
            print(" ", end="")
        print("")
        n += 1
        columns -= 1






