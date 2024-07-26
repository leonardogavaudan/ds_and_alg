from collections import deque
from typing import Dict, List, Optional


def bfs_shortest_path(
    graph: Dict[str, List[str]], start_node: str, target_node: str
) -> List[str]:
    node_to_parent_node: Dict[str, Optional[str]] = {start_node: None}
    queue = deque([start_node])
    nodes_node
