a1 = ["arp", "live", "strong"]
a3 =["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def in_array(array1, array2):
    list_in = []
    for i in array1:
        for j in array2:
            if i in j:
                list_in.append(i)
                break

    i = 0
    j = 1
    while j < len(list_in):
        if list_in[i] > list_in[j]:
            swap = list_in[i]
            list_in[i] = list_in[j]
            list_in[j] = swap
            i = 0
            j = 1
        else:
            i += 1
            j += 1

    return list_in

print(in_array(a1, a2))