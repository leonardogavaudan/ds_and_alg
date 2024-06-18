def quick_sort(lst: list[int]):
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]

    greater_than = [x for x in lst[:-1] if x >= pivot]
    less_than = [x for x in lst[:-1] if x < pivot]

    return quick_sort(less_than) + [pivot] + quick_sort(greater_than)


lst = [3, 8, 3, 7, 4, 7, 5]

sorted_lst = quick_sort(lst)
print(sorted_lst)
