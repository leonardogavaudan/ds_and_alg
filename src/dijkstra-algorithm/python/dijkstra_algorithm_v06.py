from collections import deque
from typing import Dict, List, Optional

def get_next_node(node_to_cost: Dict[str, int], processed_nodes: set[str]) -> Optional[str]:
    min_cost_node = None

    for node, cost in node_to_cost.items():
        if node not in processed_nodes and (min_cost_node is None or cost < node_to_cost[min_cost_node]): 
            min_cost_node = node

    return min_cost_node

def dijkstra_shortest_path(graph: Dict[str, Dict[str, int]], start_node: str, target_node: str) -> Optional[List[str]]:
    node_to_cost = {start_node: 0}
    node_to_parent_node = {start_node: None}
    processed_nodes = set()
    current_node = start_node

    while True:
        current_node = get_next_node(node_to_cost, processed_nodes)
        if current_node is None:
            break

        neighbor_node_to_cost = graph[current_node]

        for neighbor_node, cost in neighbor_node_to_cost.items():
            if (neighbor_node not in node_to_cost or
                node_to_cost[current_node] + cost < node_to_cost[neighbor_node]):
                node_to_cost[neighbor_node] = node_to_cost[current_node] + cost
                node_to_parent_node[neighbor_node] = current_node

        processed_nodes.add(current_node)
                
    if target_node not in node_to_cost:
        return None

    current_node = target_node
    reverse_path = []
    while current_node is not None:
        reverse_path.append(current_node)
        current_node = node_to_parent_node[current_node]

    return reverse_path[::-1]


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
