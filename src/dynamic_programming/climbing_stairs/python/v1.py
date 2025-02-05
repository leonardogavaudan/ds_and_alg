def climbing_stairs(n: int):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, b + a

    return b


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (1, 1),  # 1 step
        (2, 2),  # 2 steps: (1,1) or (2)
        (3, 3),  # 3 steps: (1,1,1), (1,2), (2,1)
        (4, 5),  # 4 steps: (1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2)
        (5, 8),  # 5 steps
    ]

    for n, expected in test_cases:
        result = climbing_stairs(n)
        assert (
            result == expected
        ), f"Test failed for n={n}. Expected {expected}, got {result}"
        print(f"n={n}: {result} ways to climb stairs")
