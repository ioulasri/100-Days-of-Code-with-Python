def alternate_sq_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if i % 2 == 1:
            sum += arr[i]**2
        else:
            sum += arr[i]
    return sum