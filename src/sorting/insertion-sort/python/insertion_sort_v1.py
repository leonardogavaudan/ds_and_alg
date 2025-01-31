from typing import List

def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        k = i
        while k > 0 and arr[k - 1] > arr[k]:
            arr[k - 1], arr[k] = arr[k], arr[k - 1]
            k -= 1

if __name__ == "__main__":
    arr = [5, 9, 8, 4, 4, 3, 2, 7]
    print(f"Original array: {arr}")
    insertion_sort(arr)
    print(f"Sorted array: {arr}")
