def longest_common_subsequence(s1: str, s2: str):
    best_lcs = 0

    def backtrack(i1: int, i2: int, current_lcs: int):
        nonlocal best_lcs, s1, s2

        if i1 == len(s1) or i2 == len(s2):
            return 0
        if current_lcs + min(len(s1) - i1, len(s2) - i2) <= best_lcs:
            return 0

        if s1[i1] == s2[i2]:
            child_current = 1 + backtrack(i1 + 1, i2 + 1, current_lcs + 1)
            best_lcs = max(best_lcs, child_current)
            return child_current
        else:
            child_current = max(
                backtrack(i1 + 1, i2, current_lcs), backtrack(i1, i2 + 1, current_lcs)
            )
            best_lcs = max(best_lcs, child_current)
            return child_current

    backtrack(0, 0, 0)
    return best_lcs


if __name__ == "__main__":
    test_cases = [
        ("ABCDGH", "AEDFHR", 3),  # Expected LCS length: 3 (ADH)
        ("AGGTAB", "GXTXAYB", 4),  # Expected LCS length: 4 (GTAB)
        ("ABCD", "ABCD", 4),  # Expected LCS length: 4 (ABCD)
        ("", "ABC", 0),  # Expected LCS length: 0
        ("XYZ", "", 0),  # Expected LCS length: 0
        ("HELLO", "WORLD", 1),  # Expected LCS length: 1 (L)
    ]

    for s1, s2, expected in test_cases:
        result = longest_common_subsequence(s1, s2)
        print(f"LCS length for '{s1}' and '{s2}': {result} (Expected: {expected})")
