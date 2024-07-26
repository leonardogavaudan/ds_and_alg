def quick_sort(lst: list[int]):
    pivot = lst[0]

    less = [x for x in lst[1:] if x <= pivot]
    greater = [x for x in lst[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
