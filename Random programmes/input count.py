count = 0
nums = []
a = 0
while True:
    row = input("Write something: ")
    if row != "end":
        nums.append(int(row))
        count += 1
    else:
        a = sum(nums) / count
        print(a)
        break
