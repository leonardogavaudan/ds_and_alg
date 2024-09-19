from typing import List, Optional


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BST:
    def __init__(self):
        self.root = None

    def insert_recursive(self, node: Optional[Node], key: int) -> Node:
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.insert_recursive(node.left, key)
        else:
            node.right = self.insert_recursive(node.right, key)

        return node

    def insert(self, key: int) -> None:
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self.insert_recursive(self.root, key)

    def get_min(self, node: Node) -> Node:
        while node.left:
            node = node.left
        return node

    def delete_recursive(self, node: Optional[Node], key: int) -> Optional[Node]:
        if node is None:
            return

        if key < node.key:
            node.left = self.delete_recursive(node.left, key)
            return node
        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)
            return node
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self.get_min(node.right)
            node.key = successor.key
            self.delete_recursive(node.right, successor.key)
            return node

    def delete(self, key: int) -> None:
        self.root = self.delete_recursive(self.root, key)

    def inorder_traversal(
        self, node: Optional[Node] = None, result: Optional[List[int]] = None
    ) -> List[int]:
        if self.root is None:
            return []
        if node is None:
            node = self.root
        if result is None:
            result = []

        if node.left:
            self.inorder_traversal(node.left, result)

        result.append(node.key)

        if node.right:
            self.inorder_traversal(node.right, result)

        return result


if __name__ == "__main__":
    bst = BST()
    nodes_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for key in nodes_to_insert:
        bst.insert(key)

    print("\nIn-order traversal before deletions:", bst.inorder_traversal())

    # Delete a leaf node
    bst.delete(20)
    print("In-order traversal after deleting 20:", bst.inorder_traversal())

    # Delete a node with one child
    bst.delete(30)
    print("In-order traversal after deleting 30:", bst.inorder_traversal())

    # Delete a node with two children
    bst.delete(50)
    print("In-order traversal after deleting 50:", bst.inorder_traversal())
