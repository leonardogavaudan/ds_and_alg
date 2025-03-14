from typing import List


def selection_sort(lst: List[int]):
    for i in range(len(lst) - 1):
        low_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[low_idx]:
                low_idx = j

        lst[i], lst[low_idx] = lst[low_idx], lst[i]


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
        selection_sort(lst)
        print(f"Sorted: {lst}\n")
