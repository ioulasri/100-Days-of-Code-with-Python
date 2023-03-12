account = {}
check = 0

def lines(statement):
    print('--------------------------------------------------------')
    print()
    print(statement)
    print()
    print('--------------------------------------------------------')

def withdraw():
    global check
    name = input("what's your account name: ")
    amount = int(input("enter amount to withdraw: "))
    for k, v in account.items():
        if k == name:
            if account[name] > amount:
                account[name] -= amount
                return
            else:
                lines("rak 7aze9")
                return
        check = 0
    lines("Incorrect name please try again")
    check = 0

def deposit():
    global check
    name = input("what's your account name: ")
    amount = int(input("enter amount to deposit: "))
    for k, v in account.items():
        if k == name:
            account[name] += amount
            return
    lines("Incorrect name please try again")
    check = 0


def open_account():
    name = input("enter your name:")
    account[name] = 0

def close_account():
    name = input("Enter your account name: ")
    account.pop(name)

def tranfer_money():
    name = input("Enter your account name: ")
    transfer_to = input("Enter the account you want to transfer money to: ")
    for k, v in account.items():
        if k == name:
            for key, value in account.items():
                if key == transfer_to:
                    amount = int(input("enter the amount you want to transfer: "))
                    if account[name] > amount:
                        account[name] -= amount
                        account[transfer_to] += amount
                        return
                    else:
                        lines("rak 7aze9")
                        return

    lines("Incorrect information please try again..")

def check_balance():
    name = input("enter your account name: ")
    check_valid = 1
    for k, v in account.items():
        if name == k:
            lines("Account name : " + name + "\nAccount balance: " + str(account[name]) + "$")
            check_valid = 0
    if check_valid == 1:
        lines("Account not found")

print("Welcome to MAROCTELECOM")
while True:
    OPTIONS = input("choose one of the given options:"
          "\n1- Open account\n2- Close account\n3- Deposit\n4- Withdraw\n5- Transfer money\n6- Check Balance\n")

    if OPTIONS == "1":
        open_account()
    if OPTIONS == "2":
        close_account()
    if OPTIONS == "3":
        deposit()
    if OPTIONS == "4":
        withdraw()
    if OPTIONS == "5":
        tranfer_money()
    if OPTIONS == "6":
        check_balance()
    print(account)
