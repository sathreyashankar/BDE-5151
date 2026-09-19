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
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def preorder(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")

    def level_order(self):
        if self.root is None:
            print("Tree is empty.")
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            print(current.data, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)


tree = BinaryTree()


while True:

    print("\n===== BINARY TREE MENU =====")
    print("1. Insert")
    print("2. Preorder Traversal")
    print("3. Inorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level Order Traversal")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        data = int(input("Enter data: "))
        tree.insert(data)

        print("Node inserted successfully.")

    elif choice == 2:

        print("Preorder Traversal:")
        tree.preorder(tree.root)
        print()

    elif choice == 3:

        print("Inorder Traversal:")
        tree.inorder(tree.root)
        print()

    elif choice == 4:

        print("Postorder Traversal:")
        tree.postorder(tree.root)
        print()

    elif choice == 5:

        print("Level Order Traversal:")
        tree.level_order()
        print()

    elif choice == 6:

        print("Exiting...")
        break

    else:

        print("Invalid choice. Please try again.")