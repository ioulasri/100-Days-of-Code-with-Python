from replit import clear
import art

print(art.logo)
high = 0
bidders = {}
name = ""
while True:
    another = input("Is there any other bidders 'y' for yes, 'n' for no: \n").lower()
    if another == 'y':
        clear()
        name = input("Add your name: ")
        bid = int(input("Enter your bid: "))
        bidders[name] = bid
        for e, f in bidders.items():
            if f > high:
                high = f


        def get_keys_from_value(val):
            return [k for k, v in bidders.items() if v == val]


        keys = get_keys_from_value(high)
        name = "".join(keys)
    else:
        break

print("The highest bidder was " + name + " with " + str(high) + "$")
