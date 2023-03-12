num_list = [i for i in range(1, 100)]

def linearSearch(numList, keyValue):
    index = 0
    while index < len(numList):
        if numList[index] == keyValue:
            return index
        index += 1
    return -1

print(linearSearch(num_list, 43))