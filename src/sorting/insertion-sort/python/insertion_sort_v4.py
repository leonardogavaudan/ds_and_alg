from typing import List


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [64, 25, 12, 22, 11],
    ]

    for i, lst in enumerate(test_cases):
        print(f"Test case {i + 1}: {lst}")
        insertion_sort(lst)
        print(f"Sorted: {lst}\n")
