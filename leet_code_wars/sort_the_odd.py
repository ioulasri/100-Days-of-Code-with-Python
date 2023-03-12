def sort_array(source_array):
    list_index = []
    list_odd = []

    for i in source_array:
        if i % 2 == 1:
            list_odd.append(i)

    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            list_index.append(i)

    i = 0
    j = 1
    while j < len(list_odd):

        if list_odd[i] > list_odd[j]:
            swap = list_odd[i]
            list_odd[i] = list_odd[j]
            list_odd[j] = swap
            i = 0
            j = 1
        else:
            i += 1
            j += 1

    j = 0
    for i in list_index:
        source_array[i] = list_odd[j]
        j += 1
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))