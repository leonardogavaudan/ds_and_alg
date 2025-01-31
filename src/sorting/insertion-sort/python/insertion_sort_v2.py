from typing import List


def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


if __name__ == "__main__":
    arr = [5, 9, 8, 4, 4, 3, 2, 7]
    print(f"Original array: {arr}")
    insertion_sort(arr)
    print(f"Sorted array: {arr}")
