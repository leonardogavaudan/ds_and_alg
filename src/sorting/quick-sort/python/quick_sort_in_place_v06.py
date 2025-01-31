from typing import List


def quick_sort_recurse(arr: List[int], low_index: int, high_index: int) -> None:
    if low_index >= high_index:
        return

    pivot = arr[high_index]
    final_pivot_index = low_index

    for i in range(low_index, high_index):
        if arr[i] < pivot:
            arr[final_pivot_index], arr[i] = arr[i], arr[final_pivot_index]
            final_pivot_index += 1

    arr[final_pivot_index], arr[high_index] = arr[high_index], arr[final_pivot_index]
    quick_sort_recurse(arr, low_index, final_pivot_index - 1)
    quick_sort_recurse(arr, final_pivot_index + 1, high_index)


def quick_sort(arr: List[int]) -> None:
    return quick_sort_recurse(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [55, 32, 11, 32, 435, 28, 47, 22]
    print("Original array: ", arr)
    quick_sort(arr)
    print("Sorted array: ", arr)
