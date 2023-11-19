def selection_sort(lst: list[int]):
    for i in range(len(lst)):
        lowest = i
        for k in range(i + 1, len(lst)):
            if lst[k] < lst[lowest]:
                lowest = k

        lst[lowest], lst[i] = lst[i], lst[lowest]

    return lst
