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
            if current_node.left is None:
                current_node.left = insert_node
            else:
                self.insert_recursive(current_node.left, insert_node)
        else:
            if current_node.right is None:
                current_node.right = insert_node
            else:
                self.insert_recursive(current_node.right, insert_node)

    def insert(self, insert_node: Node):
        if self.root is None:
            self.root = insert_node
        else:
            self.insert_recursive(self.root, insert_node)

    def search_recursive(self, current_node, key):
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self.search_recursive(current_node.left, key)
        else:
            return self.search_recursive(current_node.right, key)


    def search(self, key):
        if self.root is None:
            return None
        return self.search_recursive(self.root, key)

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def recurse_delete(self, current_node, key):
        if current_node is None:
            return None

        if key < current_node.key:
            current_node.left = self.recurse_delete(current_node.left, key)
            return current_node
        if key > current_node.key:
            current_node.right = self.recurse_delete(current_node.right, key)
            return current_node

        if current_node.left is None and current_node.right is None:
            return None 
        if current_node.left is None:
            return current_node.right
        if current_node.right is None:
            return current_node.left

        successor = self.find_min(current_node.right)
        current_node.key = successor.key
        current_node.right = self.recurse_delete(current_node.right, successor.key)

        return current_node

    
    def delete(self, key):
        self.root = self.recurse_delete(self.root, key)

    def inorder_traversal(self, node = None, result = None):
        if node is None:
            node = self.root
        if result is None:
            result = []
        
        if node.right:
            self.inorder_traversal(node.right, result)
        result.append(node.key)
        if node.left:
            self.inorder_traversal(node.left, result)

        return result


if __name__ == "__main__":
    bst = BST()
    nodes_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for key in nodes_to_insert:
        bst.insert(Node(key))

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

