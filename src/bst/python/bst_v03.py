from typing import List, Optional


class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BST:
    def __init__(self) -> None:
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
        self.root = self.insert_recursive(self.root, key)

    def find_min(self, node: Node) -> Node:
        while node.left:
            node = node.left
        return node

    def delete_recursive(self, node: Optional[Node], key: int) -> Optional[Node]:
        if node is None:
            return None

        if node.key != key:
            if key < node.key:
                node.left = self.delete_recursive(node.left, key)
            else:
                node.right = self.delete_recursive(node.right, key)

            return node
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self.find_min(node.right)
            node.key = successor.key
            node.right = self.delete_recursive(node.right, successor.key)
            return node

    def delete(self, key: int) -> None:
        self.root = self.delete_recursive(self.root, key)

    def inorder_traversal(self, res=None, node=None) -> List[int]:
        if self.root is None:
            return []

        if res is None:
            res = []
        if node is None:
            node = self.root

        if node.left:
            self.inorder_traversal(res, node.left)

        res.append(node.key)

        if node.right:
            self.inorder_traversal(res, node.right)

        return res


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
