class Node:
    flag = False
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 1

    def display_linked_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end='=>')
            current_node = current_node.next
        print(None)

    def find_middle(self):
        middle = self.head
        current = self.head

        while current.next is not None:
            middle = middle.next
            current = current.next.next
        return middle
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        if self.count > 10:
            middle_node = self.find_middle()
            print(middle_node.data)
            
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        self.count += 1


    





queue = LinkedList()

queue.insert_at_end(10)
queue.insert_at_end(20)
queue.insert_at_end(30)
queue.insert_at_end(40)
queue.insert_at_end(50)
queue.insert_at_end(60)
queue.insert_at_end(70)
queue.insert_at_end(80)
queue.insert_at_end(90)
queue.insert_at_end(100)
queue.insert_at_end(100)
queue.insert_at_end(100)

queue.display_linked_list()

