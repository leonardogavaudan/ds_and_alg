from collections import deque


def bfs(graph, start):
    seen = set()
    queue = deque()
    queue.append(start)

    while len(queue) > 0:
        current_node = queue.popleft()
        print(current_node)

        for neighbour_node in graph[current_node]:
            if neighbour_node not in seen:
                queue.append(neighbour_node)
                seen.add(neighbour_node)


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    bfs(graph, "A")
