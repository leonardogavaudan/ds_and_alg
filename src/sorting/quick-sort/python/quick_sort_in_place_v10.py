from typing import List


def quick_sort_recurse(arr: List[int], start: int, end: int):
    if start >= end:
        return

    pivot = arr[end]
    final_pivot_index = start

    for i in range(start, end):
        if arr[i] < pivot:
            arr[final_pivot_index], arr[i] = arr[i], arr[final_pivot_index]
            final_pivot_index += 1

    arr[final_pivot_index], arr[end] = arr[end], arr[final_pivot_index]

    quick_sort_recurse(arr, start, final_pivot_index - 1)
    quick_sort_recurse(arr, final_pivot_index + 1, end)


def quicksort(arr: List[int]):
    quick_sort_recurse(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [64, 25, 12, 22, 11],
        [3, 3, 3],
        [-1, -3, -2, -5, -4],
        [1, 2, 2, 1],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]

    for i, lst in enumerate(test_cases):
        print(f"Test case {i + 1}: {lst}")
        quicksort(lst)
        print(f"Sorted: {lst}\n")
