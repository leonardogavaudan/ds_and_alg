from collections import deque

# Define the graph using an adjacency list
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

# Initialize visited set to keep track of visited nodes


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


# Run BFS (You can uncomment this line when ready to test)
bfs(graph, "A")
