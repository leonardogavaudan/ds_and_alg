from typing import List, Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.next: Optional[Node] = None


class HashTable:
    def __init__(self) -> None:
        self.occupied_slots = 0
        self.total_size = 10
        self.table: List[Optional[Node]] = [None] * self.total_size

    def get_hash(self, key: int) -> int:
        return key % self.total_size

    def get(self, key: int) -> Optional[Node]:
        hash = self.get_hash(key)
        node = self.table[hash]
        while node and node.key != key:
            node = node.next

        return node

    def double_table(self) -> None:
        self.total_size = 2 * self.total_size
        self.occupied_slots = 0

        doubled_table: List[Optional[Node]] = [None] * self.total_size

        for i in range(len(self.table)):
            node = self.table[i]

            while node is not None:
                new_hash = self.get_hash(node.key)
                new_node = doubled_table[new_hash]
                if new_node is None:
                    doubled_table[new_hash] = Node(node.key, node.value)
                    self.occupied_slots += 1
                else:
                    while new_node.next is not None:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)

                node = node.next

        self.table = doubled_table

    def update(self, key: int, value: int) -> None:
        hash = self.get_hash(key)
        node = self.table[hash]

        if node is None:
            self.table[hash] = Node(key, value)
            self.occupied_slots += 1

            if self.occupied_slots / len(self.table) > 0.7:
                self.double_table()
            return
        else:
            while node is not None:
                if node.key == key:
                    node.value = value
                    break

                if node.next is None:
                    node.next = Node(key, value)
                    break

                node = node.next

    def delete(self, key: int) -> None:
        hash = self.get_hash(key)
        node = self.table[hash]
        prev = None

        while node and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return

        if prev is None:
            self.table[hash] = node.next
            if node.next is None:
                self.occupied_slots -= 1
            return

        prev.next = node.next


if __name__ == "__main__":
    hash_table = HashTable()

    # Insert some key-value pairs
    hash_table.update(1, 100)
    hash_table.update(2, 200)
    hash_table.update(3, 300)
    hash_table.update(12, 400)  # This will cause a collision with key=2

    # Retrieve and print some values
    node = hash_table.get(1)
    if node:
        print(f"Key: {node.key}, Value: {node.value}")
    else:
        print("Key not found.")

    node = hash_table.get(12)
    if node:
        print(f"Key: {node.key}, Value: {node.value}")
    else:
        print("Key not found.")

    # Update existing key
    hash_table.update(1, 500)
    node = hash_table.get(1)
    if node:
        print(f"Updated Key: {node.key}, Value: {node.value}")

    # Delete a key
    hash_table.delete(2)
    node = hash_table.get(2)
    if node:
        print(f"Key: {node.key}, Value: {node.value}")
    else:
        print("Key 2 deleted successfully.")
