from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    lesser = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i >= pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    unsorted_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", unsorted_arr)

    sorted_arr = quick_sort(unsorted_arr)
    print("Sorted array:", sorted_arr)
