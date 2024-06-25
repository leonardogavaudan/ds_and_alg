from typing import List


def selection_sort(arr: List[int]) -> None:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
