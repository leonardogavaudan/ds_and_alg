from collections import deque
from typing import Dict, List


def bfs_traversal(graph: Dict[str, List[str]], start_node: str) -> None:
    queue = deque([start_node])
    nodes_seen = set()

    while queue:
        current_node = queue.popleft()

        for neighbor_node in graph[current_node]:
            if neighbor_node not in nodes_seen:
                nodes_seen.add(neighbor_node)
                queue.append(neighbor_node)

        print(current_node)


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    bfs_traversal(graph, "A")
