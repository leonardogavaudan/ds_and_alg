from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2 :])

    l, r = 0, 0

    res = []

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            res.append(right[r])
            r += 1
        else:
            res.append(left[l])
            l += 1

    while l < len(left):
        res.append(left[l])
        l += 1

    while r < len(right):
        res.append(right[r])
        r += 1

    return res


if __name__ == "__main__":
    arr = [4, 3, 5, 9, 7, 8, 2]
    sorted_arr = merge_sort(arr)

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
