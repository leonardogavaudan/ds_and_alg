def selection_sort(lst: list[int]):
    for i in range(len(lst)):
        min = i

        for k in range(i + 1, len(lst)):
            if lst[min] > lst[k]:
                min = k

        lst[min], lst[i] = lst[i], lst[min]

    return lst


lst = [2, 8, 4, 4, 0, 9, 8, 3]

result = selection_sort(lst)

print(result)
