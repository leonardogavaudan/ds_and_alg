def dijkstra(graph, start):
    parents = {}
    current_costs = {node: float("inf") for node in graph}
    current_costs[start] = 0
    processed = set()

    current_node = find_lowest_cost_node(current_costs, processed)

    while current_node is not None:
        neighbour_nodes = graph[current_node].keys()
        neighbour_costs = graph[current_node]

        for neighbour_node in neighbour_nodes:
            new_cost = current_costs[current_node] + neighbour_costs[neighbour_node]
            if new_cost < current_costs[neighbour_node]:
                current_costs[neighbour_node] = new_cost
                parents[neighbour_node] = current_node

        processed.add(current_node)
        current_node = find_lowest_cost_node(current_costs, processed)


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs.keys():
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node

    return lowest_cost_node


if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    dijkstra(graph, "A")
