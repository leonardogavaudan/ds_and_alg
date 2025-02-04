def longest_common_subsequence(s1: str, s2: str):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    test_cases = [
        ("ABCDGH", "AEDFHR", 3),
        ("AGGTAB", "GXTXAYB", 4),
        ("HELLO", "WORLD", 1),
        ("", "ABC", 0),
        ("XYZ", "", 0),
        ("ABCDE", "ABCDE", 5),
    ]

    for s1, s2, expected in test_cases:
        result = longest_common_subsequence(s1, s2)
        print(f"String 1: {s1}")
        print(f"String 2: {s2}")
        print(f"Expected LCS length: {expected}")
        print(f"Actual LCS length: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)
