from typing import List


def longest_increasing_subsequence(arr: List[int]):
    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + 1 if arr[j] < arr[i] else 1)

    return max(dp)


if __name__ == "__main__":
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
    ]

    for arr, expected in test_cases:
        result = longest_increasing_subsequence(arr)
        print(f"Array: {arr}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"{'✓' if result == expected else '✗'}")
        print()
