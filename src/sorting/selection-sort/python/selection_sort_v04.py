def selection_sort(lst: list[int]):
    for i in range(len(lst)):
        lowest_index = i

        for k in range(i + 1, len(lst)):
            if lst[k] < lst[lowest_index]:
                lowest_index = k

        lst[i], lst[lowest_index] = lst[lowest_index], lst[i]

    return lst


lst = [3, 2, 2, 9, 7, 4, 5, 1, 1, 3]

res = selection_sort(lst)

print(res)
