def cube(arg):
    return arg ** 3


while True:
    n = input("enter a number: ")
    if n == "end":
        quit()
    else:
        print(cube(int(n)))
