from collections import deque
from typing import Dict, List, Optional


def bfs_shortest_path(
    graph: Dict[str, List[str]], starting_node: str, target_node: str
) -> Optional[List[str]]:
    node_to_parent_node: Dict[str, Optional[str]] = {starting_node: None}
    queue = deque([starting_node])
    while queue:
        current_node = queue.popleft()
        if current_node == target_node:
            reverse_shortest_path = []
            while current_node:
                reverse_shortest_path.append(current_node)
                current_node = node_to_parent_node[current_node]
            return reverse_shortest_path[::-1]
        else:
            for neighbor_node in graph[current_node]:
                if neighbor_node not in node_to_parent_node:
                    queue.append(neighbor_node)
                    node_to_parent_node[neighbor_node] = current_node


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    start_node = "A"
    target_node = "F"
    path = bfs_shortest_path(graph, start_node, target_node)
    print("Path from", start_node, "to", target_node, ":", path)
