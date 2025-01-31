def fibonacci(n: int):
    memo = {}

    def recurse(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1

        res = recurse(n - 1) + recurse(n - 2)
        memo[n] = res
        return res

    return recurse(n)


if __name__ == "__main__":
    print(f"Fibonacci number of 10 is {fibonacci(10)}")
