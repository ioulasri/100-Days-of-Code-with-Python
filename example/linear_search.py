ceil = 100000000000000
list_numbers = [i for i in range(ceil)]
start = 0
end = ceil

def binary_search(n):
    global start, end
    middle = round((start + end) / 2)
    while True:
        middle = round((start + end) / 2)
        if n == list_numbers[middle]:
            print(n)
            quit()
        if n < middle:
            end = middle
        elif n > middle:
            start = middle


binary_search(5423434324)