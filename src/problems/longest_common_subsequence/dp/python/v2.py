def longest_common_subsequence(s1: str, s2: str):
    m, n = len(s1), len(s2)

    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(curr[j - 1], prev[j])

        prev, curr = curr, prev

    return prev[n]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
        ("abc", "", 0),
        ("", "", 0),
        ("AGGTAB", "GXTXAYB", 4),
    ]

    for s1, s2, expected in test_cases:
        result = longest_common_subsequence(s1, s2)
        print(f"s1: {s1}, s2: {s2}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}\n")
