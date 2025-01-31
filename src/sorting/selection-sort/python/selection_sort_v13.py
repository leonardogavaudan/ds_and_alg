from typing import List

def selection_sort(arr: List[int]) -> None:
    for k in range(len(arr) - 1):
        min_index = k
        for i in range(k, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i

        arr[k], arr[min_index] = arr[min_index], arr[k]

    return arr

if __name__ == "__main__":
    arr = [8, 4, 19, 34,2, 3, 8, 100]
    print(f"Original string: {arr}")
    selection_sort(arr)
    print(f"Sorted string: {arr}")
