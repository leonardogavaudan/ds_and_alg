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
