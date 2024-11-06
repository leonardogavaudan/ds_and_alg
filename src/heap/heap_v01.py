from typing import List, Optional


def heapify(arr: List[int], n: int, i: int) -> None:
    smallest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def build_heap(arr: List[int]) -> List[int]:
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)
    return arr


def insert(arr: List[int], key: int) -> None:
    arr.append(key)
    i = len(arr) - 1
    while i > 0 and arr[i] < arr[(i - 1) // 2]:
        arr[(i - 1) // 2], arr[i] = arr[i], arr[(i - 1) // 2]
        i = (i - 1) // 2


def pop(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None

    res = arr[0]
    arr[0] = arr[-1]
    arr.pop()

    i = 0
    while i < len(arr):
        left_i = i * 2 + 1
        right_i = i * 2 + 2

        smallest = i
        if left_i < len(arr) and arr[left_i] < arr[smallest]:
            smallest = left_i
        if right_i < len(arr) and arr[right_i] < arr[smallest]:
            smallest = right_i

        if smallest == i:
            break

        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest

    return res


if __name__ == "__main__":
    # Create a sample heap (min-heap)
    heap = []

    # Insert elements into the heap
    elements_to_insert = [10, 20, 5, 15, 30, 2, 25]
    print("Inserting elements:", elements_to_insert)
    for el in elements_to_insert:
        insert(heap, el)
        print(f"Heap after inserting {el}: {heap}")

    # Pop elements from the heap
    print("\nPopping elements:")
    while heap:
        popped = pop(heap)
        print(f"Popped: {popped}, Heap after pop: {heap}")
