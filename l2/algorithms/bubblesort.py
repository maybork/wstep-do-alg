def bubblesort(to_sort: list) -> list:
    listlen = len(to_sort)
    for i in range(listlen):
        for j in range(listlen - i - 1):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    return to_sort


def bubblesort_smart(to_sort: list) -> list:
    listlen = len(to_sort)
    for i in range(listlen):
        done = True
        for j in range(listlen - i - 1):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
                done = False
        if done:
            break
    return to_sort


def bubblesort_naive(to_sort: list) -> list:
    listlen = len(to_sort)
    for i in range(listlen):
        for j in range(listlen - 1):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    return to_sort
