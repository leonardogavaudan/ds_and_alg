def selection_sort(lst: list[int]) -> list[int]:
    for i_1, _ in enumerate(lst):
        min_index = i_1

        for i_2 in range(i_1 + 1, len(lst)):
            if lst[i_2] < lst[min_index]:
                min_index = i_2

        lst[i_1], lst[min_index] = lst[min_index], lst[i_1]

    return lst


sorted_list = selection_sort([23, 57, 12, 9, 45])

print(sorted_list)
