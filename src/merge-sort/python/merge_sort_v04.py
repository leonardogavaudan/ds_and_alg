from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return [arr[0], arr[1]] if arr[0] < arr[1] else [arr[1], arr[0]]

    res = []

    left = merge_sort(arr[: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2 :])

    i, j = 0, 0
    while i < len(left) and j < len(left):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1

    return res


if __name__ == "__main__":
    arr = [4, 3, 5, 9, 7, 8, 2]
    sorted_arr = merge_sort(arr)

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
