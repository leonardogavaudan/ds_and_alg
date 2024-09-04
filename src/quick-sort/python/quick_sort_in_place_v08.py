from typing import List

def quick_sort_recurse(arr: List[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot = arr[high]
    pivot_final_index = low

    for i in range(low, high):
        if arr[i] < pivot:
            arr[pivot_final_index], arr[i] = arr[i], arr[pivot_final_index]
            pivot_final_index += 1

    arr[pivot_final_index], arr[high] = arr[high], arr[pivot_final_index]

    quick_sort_recurse(arr, low, pivot_final_index - 1)
    quick_sort_recurse(arr, pivot_final_index + 1, high)

def quick_sort(arr: List[int]) -> None:
    quick_sort_recurse(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [48, 22, 19, 48, 47, 273, 37]
    print(f"Original array: {arr}")
    quick_sort(arr)
    print(f"Sorted array: {arr}")
