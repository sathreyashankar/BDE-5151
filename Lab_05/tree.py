from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            if current.left is None:
                self.root = new_node
                return
            else:
                queue.append(current.node)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)


tree = BinaryTree()

for value in [10, 20, 30, 40, 50, 60, 70, 80]:
    tree.insert(value)