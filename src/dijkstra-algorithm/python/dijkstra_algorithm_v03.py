from typing import Dict, List, Optional


def find_lowest_cost_node(
    node_to_cost: Dict[str, int], nodes_processed: set[str]
) -> Optional[str]:
    min_node = None
    min_cost = None
    for node, cost in node_to_cost.items():
        if (min_cost is None or min_cost > cost) and node not in nodes_processed:
            min_node = node
            min_cost = cost
    return min_node


def dijkstra_shortest_path(
    graph: Dict[str, Dict[str, int]], starting_node: str, target_node: str
) -> Optional[List[str]]:
    node_to_cost = {starting_node: 0}
    node_to_parent_node: Dict[str, Optional[str]] = {starting_node: None}
    nodes_processed = set()
    current_node = starting_node
    while current_node:
        for neighbor_node in graph[current_node].keys():
            if (neighbor_node not in node_to_cost) or (
                node_to_cost[current_node] + graph[current_node][neighbor_node]
                < node_to_cost[neighbor_node]
            ):
                node_to_cost[neighbor_node] = (
                    node_to_cost[current_node] + graph[current_node][neighbor_node]
                )
                node_to_parent_node[neighbor_node] = current_node
        nodes_processed.add(current_node)
        current_node = find_lowest_cost_node(node_to_cost, nodes_processed)

    if target_node not in node_to_cost:
        return

    current_node = target_node
    reverse_short_path = []
    while current_node:
        reverse_short_path.append(current_node)
        current_node = node_to_parent_node[current_node]

    return reverse_short_path[::-1]


if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }

    # Test case 1: A to D
    result = dijkstra_shortest_path(graph, "A", "D")
    print("Shortest path from A to D:", result)
    print("Expected: ['A', 'B', 'C', 'D']")

    # Test case 2: A to C
    result = dijkstra_shortest_path(graph, "A", "C")
    print("\nShortest path from A to C:", result)
    print("Expected: ['A', 'B', 'C']")

    # Test case 3: D to A
    result = dijkstra_shortest_path(graph, "D", "A")
    print("\nShortest path from D to A:", result)
    print("Expected: ['D', 'C', 'B', 'A']")

    # Test case 4: A to A (same node)
    result = dijkstra_shortest_path(graph, "A", "A")
    print("\nShortest path from A to A:", result)
    print("Expected: ['A']")

    # Test case 5: A to E (non-existent node)
    graph_with_unreachable = graph.copy()
    graph_with_unreachable["E"] = {}
    result = dijkstra_shortest_path(graph_with_unreachable, "A", "E")
    print("\nShortest path from A to E (unreachable):", result)
    print("Expected: None")
