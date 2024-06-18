def quick_sort(lst: list[int]):
    if len(lst) < 2:
        return lst

    pivot = lst[0]

    less = [i for i in lst[1:] if i <= pivot]
    greater = [i for i in lst[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


lst = [3, 4, 9, 7, 3, 3, 1, 8, 7, 4, 9]
res = quick_sort(lst)

print(res)
