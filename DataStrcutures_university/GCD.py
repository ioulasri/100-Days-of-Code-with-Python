first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

answer = 1
divisor = 2
while divisor <= first and divisor <= second:
    if first % divisor == 0 and second % divisor == 0:
        answer = divisor
    divisor += 1

print(answer)