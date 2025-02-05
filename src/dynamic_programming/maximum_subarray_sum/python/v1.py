from itertools import islice
from typing import List


def maximum_subarray(arr: List[int]):
    max_sum = current_sum = arr[0]
    for num in islice(arr, 1, None):
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Expected: 6
        [1],  # Expected: 1
        [-1, -2, -3, -4],  # Expected: -1
        [5, 4, -1, 7, 8],  # Expected: 23
    ]
    expected_results = [6, 1, -1, 23]

    for i, (test, expected) in enumerate(zip(test_cases, expected_results), 1):
        result = maximum_subarray(test)
        print(f"Test case {i}: {test}")
        print(f"Maximum subarray sum: {result}")
        print(f"Expected result: {expected}\n")
