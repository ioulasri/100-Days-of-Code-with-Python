import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print("The coffee machine is ON!")
water = 1000
coffee = 250
milk = 300
money = 0


while True:
    options = input("What would you like? (espresso/latte/cappuccino):").lower()
    if options == "report":
        clear_screen()
        print("Your resources are: ")
        print(f"-Water: {water}ml\n-Coffee: {coffee}g\n-Milk: {milk}ml\n-Money: {money}$")
    elif options == "espresso":
        clear_screen()
        if coffee < 18:
            if water < 50:
                print("Sorry there's not enough water..")
                quit()
            print("Sorry there's not enough coffee..")
            quit()
        pennies = int(input("Insert your pennies: ")) # pennies = 0.01$
        nickles = int(input("Insert your nickles: ")) #  nickles = 0.05$
        dimes = int(input("Insert your dimes: ")) # dimes = 0.1$
        quarters = int(input("Insert your quarters: ")) # quarters = 0.25$
        coin_check = (pennies / 100) + (nickles / 20) + (dimes / 10) + (quarters / 4)
        if coin_check < 1.5:
            print("Sorry that's not enough money. Money refunded.")
        if coin_check >= 1.5:
            change = round(coin_check - 1.5, 2)
            money += 1.5
            water -= 50
            coffee -= 18
            print(f"Here's your change: {change}$")
            print("Here is your espresso. Enjoy!")
    elif options == "latte":
        clear_screen()
        if milk < 150:
            if coffee < 24:
                if water < 200:
                    print("Sorry there's not enough water..")
                    quit()
                print("Sorry there's not enough coffee..")
                quit()
            print("Sorry there's not enough milk..")
            quit()
        pennies = int(input("Insert your pennies: "))
        nickles = int(input("Insert your nickles: "))
        dimes = int(input("Insert your dimes: "))
        quarters = int(input("Insert your quarters: "))
        coin_check = (pennies / 100) + (nickles / 20) + (dimes / 10) + (quarters / 4)
        if coin_check < 2.5:
            print("Sorry that's not enough money. Money refunded.")
        if coin_check >= 2.5:
            change = round(coin_check - 2.5, 2)
            money += 2.5
            water -= 200
            coffee -= 24
            milk -= 150
            print(f"Here's your change: {change}$")
            print("Here is your latte. Enjoy!")

    elif options == "cappuccino":
        clear_screen()
        if milk < 100:
            if coffee < 24:
                if water < 250:
                    print("Sorry there's not enough water..")
                    quit()
                print("Sorry there's not enough coffee..")
                quit()
            print("Sorry there's not enough milk..")
            quit()
        pennies = int(input("Insert your pennies: "))
        nickles = int(input("Insert your nickles: "))
        dimes = int(input("Insert your dimes: "))
        quarters = int(input("Insert your quarters: "))
        coin_check = (pennies / 100) + (nickles / 20) + (dimes / 10) + (quarters / 4)
        if coin_check < 3:
            print("Sorry that's not enough money. Money refunded.")
        if coin_check >= 3:
            change = round(coin_check - 3, 2)
            money += 3
            water -= 250
            coffee -= 24
            milk -= 100
            print(f"Here's your change: {change}$")
            print("Here is your cappuccino. Enjoy!")
