from calculator import art
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear_screen()
    print(art.logo)
    num1 = float(input("Enter the first number: "))
    for k, v in operations.items():
        print(k)
    picked_operation = input("Pick an operation from line above:\n")
    num2 = float(input("Enter the second number: "))

    calculation_function = operations[picked_operation]
    first_answer = calculation_function(num1, num2)
    last_answer = first_answer
    print(f"The result is: {last_answer}\n\n")
    while True:
        user_choice = input(f"To calculate over {last_answer} press 'y', to start all over again press 'n'\n").lower()
        if user_choice == 'y':
            pick_other_op = input("Pick an operator from above again:\n")
            num3 = float(input("Enter the second number: "))
            calculation_function = operations[pick_other_op]
            second_answer = calculation_function(last_answer, num3)
            last_answer = second_answer
            print(f"The result is: {last_answer}\n\n")
        if user_choice == 'n':
            calculator()


calculator()
