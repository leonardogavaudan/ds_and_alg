def selection_sort(lst: list[int]):
    for k in range(len(lst)):
        min_index = k

        for j in range(k + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[min_index], lst[k] = lst[k], lst[min_index]

    return lst


lst = [1, 4, 5, 8, 4, 8, 4, 5, 9, 3]
sorted_lst = selection_sort(lst)

print(sorted_lst)
