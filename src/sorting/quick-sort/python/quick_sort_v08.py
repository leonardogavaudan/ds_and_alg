from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    lesser = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    arr = [28, 22, 13, 33, 993, 47, 53, 44]
    sorted_array = quick_sort(arr)
    print("Original array: ", arr)
    print("Sorted array: ", sorted_array)
