from typing import List


def count_sort(arr: List[int], exp: int) -> None:
    count = [0] * 10
    result = [0] * len(arr)

    for i in range(len(arr)):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        result[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = result[i]


def radix_sort(arr: List[int]) -> None:
    max_value = max(arr)

    exp = 1
    while max_value // exp > 0:
        count_sort(arr, exp)
        exp *= 10


if __name__ == "__main__":
    arr = [329, 457, 657, 839, 436, 720, 355]
    print("Original array:", arr)

    radix_sort(arr)
    print("Sorted array:", arr)
