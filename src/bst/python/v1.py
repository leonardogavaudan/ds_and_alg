from typing import Optional

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, root: Optional[Node] = None):
        self.root = root

    def insert_recursive(self, current_node: Node,  insert_node: Node):
        if insert_node.key < current_node.key:
            if current_node.left == None:
                current_node.left = insert_node
            else:
                self.insert_recursive(current_node.left, insert_node)
        else:
            if current_node.right == None:
                current_node.right = insert_node
            else:
                self.insert_recursive(current_node.right, insert_node)

    def insert(self, insert_node: Node):
        if self.root == None:
            self.root = insert_node
        else:
            self.insert_recursive(self.root, insert_node)

    def search_recursive(self, current_node, key):
        if current_node == None:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self.search_recursive(current_node.left, key)
        else:
            return self.search_recursive(current_node.right, key)


    def search(self, key):
        if self.root == None:
            return None
        return self.search_recursive(self.root, key)
