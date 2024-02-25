from collections import deque


def bfs_shortest_path(graph, start, goal):
    queue = deque([start])
    visited = {}
    predecessor = {start: None}

    while queue:
        node = queue.popleft()

        if node == goal:
            path = []

            while node is not None:
                path.append(node)
                node = predecessor[node]

            return path[::-1]

        if node not in visited:
            for neighbour_node in graph[node]:
                if neighbour_node not in predecessor:
                    predecessor[neighbour_node] = node
                    queue.append(neighbour_node)

    return None


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

start_node = "A"
goal_node = "F"

path = bfs_shortest_path(graph, start_node, goal_node)
print("Shortest path:", path)
