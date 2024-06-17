from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    unsorted_array = [5, 2, 9, 1, 7, 6, 3, 8, 4]
    sorted_array = quick_sort(unsorted_array)
    print("Unsorted array:", unsorted_array)
    print("Sorted array:", sorted_array)
