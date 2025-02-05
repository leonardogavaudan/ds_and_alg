from typing import List


def longest_bitonic_subsequence(arr: List[int]):
    dp_increasing = [1] * len(arr)
    dp_decreasing = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            dp_increasing[i] = max(
                dp_increasing[i], 1 + dp_increasing[j] if arr[j] < arr[i] else 1
            )

    for i in range(len(arr) - 1, -1, -1):
        for j in range(i + 1, len(arr)):
            dp_decreasing[i] = max(
                dp_decreasing[i], 1 + dp_decreasing[j] if arr[j] < arr[i] else 1
            )

    return max(
        (dp_increasing[i] if i >= 0 else 0)
        + (dp_decreasing[i + 1] if i + 1 < len(arr) else 0)
        for i in range(-1, len(arr))
    )


if __name__ == "__main__":
    # Test cases with expected results
    test_cases = [
        ([1, 11, 2, 10, 4, 5, 2, 1], 6),  # 1, 2, 10, 4, 2, 1
        ([1, 2, 3, 4, 5], 5),  # 1, 2, 3, 4, 5
        ([5, 4, 3, 2, 1], 5),  # 5, 4, 3, 2, 1
        ([1, 3, 5, 4, 2], 5),  # 1, 3, 5, 4, 2
        ([], 0),  # empty array
        ([1], 1),  # single element
    ]

    for arr, expected in test_cases:
        result = longest_bitonic_subsequence(arr)
        print(f"Array: {arr}")
        print(f"Longest bitonic subsequence length: {result}")
        print(f"Expected length: {expected}")
        print()
