Lan = {'Imad': 97, 'Ayoub': 31, 'Ahmed': 60, 'John': 90}
print(Lan)

for key, value in Lan.items():
    if value >= 90:
        value = "Outstanding"
    elif 75 <= value < 90:
        value = "Good"
    elif 50 <= value < 75:
        value = "Pass"
    else:
        value = "Fail"
    print(key + "'s grade is " + value)
