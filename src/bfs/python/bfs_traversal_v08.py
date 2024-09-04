from collections import deque
from typing import Dict, List


def bfs_traversal(graph: Dict[str, List[str]], start_node: str) -> None:
    queue = deque([start_node])
    seen = set()

    while queue:
        current_node = queue.popleft()
        print(current_node, " ")

        for neighbor_node in graph[current_node]:
            if neighbor_node not in seen:
                queue.append(neighbor_node)
                seen.add(neighbor_node)


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    bfs_traversal(graph, "A")
