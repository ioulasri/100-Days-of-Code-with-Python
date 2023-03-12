passed = []
not_passed = []
A = ""
B = ""
C = ""
D = ""
E = ""
F = ""
going = True
while going:
    grade = float(input("Enter your grade: "))
    if grade == -1:
        going = False
    elif grade < 10:
        not_passed.append(grade)
        print("failed")
        F += "*"
    elif grade < 12:
        passed.append(grade)
        print("Not bad")
        E += "*"
    elif grade < 14:
        passed.append(grade)
        print("Ok")
        D += "*"
    elif grade < 16:
        passed.append(grade)
        print("Quite good")
        C += "*"
    elif grade < 18:
        passed.append(grade)
        print("Good")
        B += "*"
    elif grade >= 18:
        passed.append(grade)
        print("Perfect")
        A += "*"

average = (sum(passed) + sum(not_passed)) / (len(passed) + len(not_passed))
passing = sum(passed) / len(passed)
pass_perc = (len(passed) * 100) / (len(passed) + len(not_passed))
print("Point average (all): " + str(round(average, 2)))
print("Point average (passing): " + str(round(passing, 2)))
print("Pass percentage: " + str(round(pass_perc, 2)))
print(f"""
Grade distribution:
5: {A}
4: {B}
3: {C}
2: {D}
1: {E}
0: {F}""")
