import math


def write_eq(delta, x, c, x2):
    if delta > 0:
        if x > 0 and c > 0 and x2 > 0:
            print(f"Your equation looks like this: {x2}x^2 + {x}x + {c}")
        elif x < 0 and c > 0 and x2 > 0:
            print(f"Your equation looks like this: {x2}x^2 - {x}x + {c}")
        elif x < 0 and c < 0 and x2 > 0:
            print(f"Your equation looks like this: {x2}x^2 - {x}x - {c}")
        elif x < 0 and c < 0 and x2 < 0:
            print(f"Your equation looks like this: -{x2}x^2 - {x}x - {c}")
        elif x < 0 and c > 0 and x2 > 0:
            print(f"Your equation looks like this: {x2}x^2 - {x}x + {c}")
        elif x > 0 and c > 0 and x2 > 0:
            print(f"Your equation looks like this: {x2}x^2 + {x}x - {c}")


print("*WELCOME TO MATHEMATICS PORTAL*")
eq_type = input("Which equation do you want to solve?\n1. First degree equation\n2. Second degree equation\n- Choose "
                "1 or 2:")
if eq_type == "1":
    x = float(input("What is the number in front of x: "))
    c = float(input("What is the constant following the x value: "))
    result = -c / x
    print("the solution for this equation is: " + str(result))

elif eq_type == "2":
    x2 = float(input("What is the number in front of x^2: "))
    x = float(input("What is the number in front of x: "))
    c = float(input("What is the constant following the x value: "))

    delta = (x ** 2) - (4 * x2 * c)
    if delta > 0:
        write_eq(delta, x, c, x2)
        print("There is two solutions for this equation")
        x_1 = (-x - math.sqrt(delta)) / (x2 * 2)
        x_2 = (-x + math.sqrt(delta)) / (2 * x2)
        print("x_1 = " + str(x_1))
        print("x_2 = " + str(x_2))
    elif delta == 0:
        write_eq(delta, x, c, x2)
        print("There is one solution for this equation")
        x_1 = -x / 2 * x2
        print("x_1 = " + str(x_1))
    else:
        write_eq(delta, x, c, x2)
        print("There is no solution for this equation.")
