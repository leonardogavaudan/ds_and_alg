from typing import List


def quick_sort_recurse(arr: List[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot = arr[high]
    final_pivot_index = low

    for i in range(low, high):
        if arr[i] < pivot:
            arr[final_pivot_index], arr[i] = arr[i], arr[final_pivot_index]
            final_pivot_index += 1

    arr[final_pivot_index], arr[high] = arr[high], arr[final_pivot_index]

    quick_sort_recurse(arr, low, final_pivot_index - 1)
    quick_sort_recurse(arr, final_pivot_index + 1, high)


def quick_sort(arr: List[int]) -> None:
    quick_sort_recurse(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [48, 22, 19, 48, 47, 273, 37]
    print(f"Original array: {arr}")
    quick_sort(arr)
    print(f"Sorted array: {arr}")
