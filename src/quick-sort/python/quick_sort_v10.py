from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    pivot = arr[-1]
    lesser = [i for i in arr[:-1] if i <= pivot]
    greater = [i for i in arr[:-1] if i > pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    arr = [48, 84, 1, 443, 22, 234, 22]
    print(f"Original array: {arr}")
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")

