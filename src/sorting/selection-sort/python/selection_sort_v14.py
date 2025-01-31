from typing import List


def selection_sort(arr: List[int]) -> None:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    arr = [8, 4, 19, 34, 2, 3, 8, 100]
    print(f"Original string: {arr}")
    selection_sort(arr)
    print(f"Sorted string: {arr}")
