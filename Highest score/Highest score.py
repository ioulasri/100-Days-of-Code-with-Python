scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0

for i in scores:
    if i > highest_score:
        highest_score = i


print("the highest score is:" + str(highest_score))
