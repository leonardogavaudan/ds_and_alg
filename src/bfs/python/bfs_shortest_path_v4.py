from collections import deque
from typing import Dict, List, Optional


def bfs(
    graph: Dict[str, List[str]], start_node: str, target_node: str
) -> Optional[List[str]]:
    node_to_parent_node: Dict[str, Optional[str]] = {start_node: None}
    queue = deque([start_node])
    while queue:
        current_node = queue.popleft()
        if current_node == target_node:
            reverse_path = []
            while current_node:
                reverse_path.append(current_node)
                current_node = node_to_parent_node[current_node]
            return reverse_path[::-1]
        else:
            for neighbour_node in graph[current_node]:
                if neighbour_node not in node_to_parent_node:
                    queue.append(neighbour_node)
                    node_to_parent_node[neighbour_node] = current_node


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    start_node = "A"
    target_node = "F"
    path = bfs(graph, start_node, target_node)
    print("Path from", start_node, "to", target_node, ":", path)
