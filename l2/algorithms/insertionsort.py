def insertionsort(to_sort: list) -> list:
    listlen = len(to_sort)
    for i in range(listlen):
        for j in range(i):
            if to_sort[i] < to_sort[j]:
                temp = to_sort[i]
                to_sort[i] = to_sort[j]
                to_sort[j] = temp
    return to_sort


# print(insertionsort([2, 562, 15, 6, 1, 6, 3, 2]))
