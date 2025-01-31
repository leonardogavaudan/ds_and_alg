from typing import List


def knapsack(W: int, weights: List[int], values: List[int]) -> List[int]:
    N = len(weights)
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    res_indices = []
    w = W
    for i in range(N, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            res_indices.append(i - 1)
            w -= weights[i - 1]

    return res_indices[::-1]


if __name__ == "__main__":
    W = 10
    weights = [1, 3, 4, 5]
    values = [10, 40, 50, 70]
    result = knapsack(W, weights, values)
    print(result)
