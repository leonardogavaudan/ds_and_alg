from typing import List


def insert(arr: List[int], key: int) -> None:
    arr.append(key)
    i = len(arr) - 1

    while i > 0:
        parent = (i - 1) // 2
        if arr[parent] < arr[i]:
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def pop(arr: List[int]) -> int:
    if len(arr) == 0:
        raise IndexError("Cannot pop off an empty heap")

    if len(arr) == 1:
        return arr.pop()

    res = arr[0]
    arr[0] = arr.pop()

    i = 0

    while i < len(arr):
        left = i * 2 + 1
        right = i * 2 + 2
        smallest = i

        if left < len(arr) and arr[left] < arr[smallest]:
            smallest = left
        if right < len(arr) and arr[right] < arr[smallest]:
            smallest = right

        if i == smallest:
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
