sum = 0
sum_1 = 0

# First method:
for i in range(101):
    if i % 2 == 0:
        sum += i

print(f'the sum of even numbers is {sum}')

# Second method:
for i in range(0, 101, 2):
    sum_1 += i

print(f'the sum of even numbers is {sum_1}')
