from collections import deque
from typing import Dict, List


def bfs_traversal(graph: Dict[str, List[str]], start: str) -> None:
    nodes_seen = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        print(current_node, " ")
        for neighbor_node in graph[current_node]:
            if neighbor_node not in nodes_seen:
                queue.append(neighbor_node)
                nodes_seen.add(neighbor_node)


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    bfs_traversal(graph, "A")
