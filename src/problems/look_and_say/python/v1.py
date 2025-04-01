def look_and_say(n: int):
    state = ["1"]
    for _ in range(n - 1):
        next_state = []
        count = 0
        char = state[0]
        for i in range(len(state)):
            if state[i] == char:
                count += 1
            else:
                next_state.append(str(count))
                next_state.append(char)
                char = state[i]
                count = 1

            if i == len(state) - 1:
                next_state.append(str(count))
                next_state.append(char)

        state = next_state

    return "".join(state)


if __name__ == "__main__":
    test_cases = [x for x in range(1, 20)]
    for n in test_cases:
        result = look_and_say(n)
        print(f"look_and_say({n}) = {result}")
