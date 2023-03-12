def is_leap(given_year):
    if given_year % 4 == 0:
        if given_year % 100 == 0:
            if given_year % 400 == 0:
                e = "Leap year".lower()
            else:
                e = "Not leap year".lower()
        else:
            e = "Leap year".lower()
    else:
        e = "Not leap year".lower()
    return e


def days_in_month(a, b):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(a) == "leap year":
        month_days[1] = 29
        return "year" + ": " + str(a) + "\n" + "Month" + ": " + str(b) + \
               "\n" + "there is " + str(month_days[b - 1]) + " days in " + '0' + str(b) + "/" + str(a)
    else:
        return "year" + ": " + str(a) + "\n" + "Month" + ": " + str(b) + \
               "\n" + "there is " + str(month_days[b - 1]) + " days in " + '0' + str(b) + "/" + str(a)


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
