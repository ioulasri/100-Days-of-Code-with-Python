from replit import clear

contact = {}
name = ""
phone_num = ""
options = input("Welcome to your contact\n-To add a number press 'a'\n-To check your contact list press 'c'\n-To "
                "look for a number press 'l'\n-To quit press 'q'\n").lower()
while True:
    if options == 'q':
        print("Good bye!")
        quit()
    if options == 'a':
        name = input("Enter your contact name:\n").title()
        phone_num = input("Enter your contact number:\n")
        contact[name] = phone_num
        clear()
    if options == 'c':
        clear()
        print("Your contacts are:")
        for k, v in contact.items():
            print("-" + str(k) + ' : ' + str(v))
    if options == 'l':
        clear()
        number = input("Enter the name of your contact").title()
        for k, v in contact.items():
            if k == number:
                print("-" + str(k) + ' : ' + str(v))
    print("\n\n\n\n")
    again = input("Do you want to see the options again\n-Type 'y' for yes\n-Type 'n' for no to quit\n").lower()
    if again == 'y':
        options = input(
            "Welcome to your contact\n-To add a number press 'a'\n-To check your contact list press 'c'\n-To "
            "look for a number press 'l'\n-To quit press 'q'\n").lower()