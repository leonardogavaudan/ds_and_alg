from collections import deque
from typing import Dict, List, Optional


def bfs_shortest_path(
    graph: Dict[str, List[str]], start_node: str, target_node: str
) -> Optional[List]:
    seen = set()
    queue = deque([start_node])
    node_to_parent_node: Dict[str, Optional[str]] = {start_node: None}

    while queue:
        current_node = queue.popleft()
        if current_node == target_node:
            reverse_path = []
            while current_node is not None:
                reverse_path.append(current_node)
                current_node = node_to_parent_node[current_node]
            return reverse_path[::-1]

        for neighbor_node in graph[current_node]:
            if neighbor_node not in seen:
                queue.append(neighbor_node)
                seen.add(neighbor_node)
                node_to_parent_node[neighbor_node] = current_node


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    start_node = "A"
    target_node = "F"
    path = bfs_shortest_path(graph, start_node, target_node)
    print("Path from", start_node, "to", target_node, ":", path)
