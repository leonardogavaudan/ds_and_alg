from collections import deque


def bfs(graph, start, target):
    queue = deque([start])
    node_to_parent_node = {start: None}

    while len(queue):
        current_node = queue.popleft()

        if current_node == target:
            reverse_parent = []

            while current_node is not None:
                reverse_parent.append(current_node)
                current_node = node_to_parent_node[current_node]

            return reverse_parent[::-1]

        for neighbour in graph[current_node]:
            if neighbour in node_to_parent_node:
                continue

            node_to_parent_node[neighbour] = current_node
            queue.append(neighbour)

    return None


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
start_node = "A"
target_node = "F"
path = bfs(graph, start_node, target_node)

print("Path from", start_node, "to", target_node, ":", path)
