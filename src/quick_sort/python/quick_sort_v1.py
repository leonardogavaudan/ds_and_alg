def quick_sort_recurse(my_list: list[int], low: int, high: int):
    if len(my_list) == 1:
        return my_list

    pivot = my_list[high - 1]
    pivot_final_index = low

    for j in range(low, high):
        if my_list[j] < pivot:
            my_list[pivot_final_index], my_list[j] = (
                my_list[j],
                my_list[pivot_final_index],
            )
            pivot_final_index += 1

    my_list[high - 1], my_list[pivot_final_index] = (
        my_list[pivot_final_index],
        my_list[high - 1],
    )

    quick_sort_recurse(my_list, low, pivot_final_index - 1)
    quick_sort_recurse(my_list, pivot_final_index + 1, high)


def quick_sort(my_list: list[int]):
    low = 0
    high = len(my_list) - 1

    quick_sort_recurse(my_list, low, high)
