from typing import Dict, List


def dijkstra_shortest_path(
    graph: Dict[str, Dict[str, int]], starting_node: str
) -> List[str]:
    node_to_cost = {}
    node_to_parent_node = {starting_node: None}
    processed = set()

    return []


if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    dijkstra_shortest_path(graph, "A")
