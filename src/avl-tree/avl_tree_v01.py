from typing import List, Optional


class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.height = 0


class AVL:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def get_height(self, node: Optional[Node]) -> int:
        if node is None:
            return -1

        return node.height

    def get_balance(self, node: Node) -> int:
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y: Node) -> Node:
        if y.left is None:
            raise IndexError("Cannot perform right rotate on node without left child")

        x = y.left
        mid = x.right

        x.right = y
        y.left = mid

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, y: Node) -> Node:
        if y.right is None:
            raise IndexError("Cannot perform left rotate on node without right child")

        x = y.right
        mid = x.left

        x.left = y
        y.right = mid

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def insert_recursive(self, node: Optional[Node], key: int) -> Node:
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert_recursive(node.left, key)
        else:
            node.right = self.insert_recursive(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance_factor = self.get_balance(node)

        if balance_factor > 1 and (node.left and key < node.left.key):
            return self.right_rotate(node)

        if balance_factor < -1 and (node.right and key > node.right.key):
            return self.left_rotate(node)

        if balance_factor > 1 and (node.left and key > node.left.key):
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance_factor < -1 and (node.right and key < node.right.key):
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, key: int) -> None:
        self.root = self.insert_recursive(self.root, key)

    def preorder_traversal(self, res=None, node=None) -> List[int]:
        if self.root is None:
            return []

        if res is None:
            res = []
        if node is None:
            node = self.root

        res.append(node.key)
        if node.left:
            self.preorder_traversal(res, node.left)
        if node.right:
            self.preorder_traversal(res, node.right)

        return res


if __name__ == "__main__":
    avl = AVL()
    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        avl.insert(key)

    print("Pre-order traversal of the AVL tree:", avl.preorder_traversal())
