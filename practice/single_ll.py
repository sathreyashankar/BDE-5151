class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_front(self):
        if self.head is None:
            print('Empty List, nothing to delete!')
            return
        print('Deleted Node: ', self.head.data)
        self.head = self.head.next
        return

    def delete_end(self):
        if self.head is None:
            print('Empty List, nothing to delete!')
            return

        if self.head.next is None:
            print('Deleted Node: ', self.head.data)
            self.head = None
            return
        
        current = self.head
        while current.next.next is not None:
            current = current.next
        print('Deleted Node: ', current.next.data)
        current.next = None

    def insert_at_index(self, data, index):
        current = self.head
        if index<0:
            print('Invalid Index!')
            return 
        if index == 0:
            self.insert_front(data)
            return
        current = self.head
        for i in range(0, index-1):
            if current is None:
                print('Invalid Index!!')
                return
            current = current.next

        if current is None:
            print('Invalid Index!!')
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if index<0 or self.head is None:
            print('Empty LinkedList, Nothing to Delete!!')
            return
        if index == 0:
            self.delete_front()
            return

        current = self.head
        for i in range(0, index-1):
            if current is None:
                print('Invalid Index!!')
                return
            current = current.next

        if current is None or current.next is None:
            print('Invalid Index!!')
            return

        print('Deleted Node: ', current.next.data)
        current.next = current.next.next


    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next

        print('Length of the Linked List:', count)


    def search(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.data == value :
                print('Found at index: ', index)
                return
            current = current.next
            index += 1

        print('Vaue not found!!')
        return

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=' --> ')
            current = current.next

        print('None')
        

sll = SinglyLinkedList()

while True:
    print('#### Singly Linked List ####')
    print('1. Insert at Front')
    print('2. Insert at End')
    print('3. Deletion at Front')
    print('4. Deletion at End')
    print('5. Insert at Index')
    print('6. Deletion at Index')
    print('7. Display Linked List Elements')
    print('8. Size of the Linked List')
    print('9. Search by Value')
    print('10. Exit')

    try:
        choice = int(input('Enter choice: '))

        match choice:
            case 1:
                data = int(input('Enter the data of a new node to be inserted at front: '))
                sll.insert_front(data)
            case 2:
                data = int(input('Enter the data of a new node to be inserted at end: '))
                sll.insert_end(data)
            case 3:
                sll.delete_front()
            case 4:
                sll.delete_end()
            case 5:
                index = int(input('Enter the index for the new node to be inserted: '))
                data = int(input(f'Enter the data of a new node to be inserted at {index}: '))
                sll.insert_at_index(data, index)
            case 6:
                index = int(input('Enter the index of the node to be deleted: '))
                sll.delete_at_index(index)
            case 7:
                print('Elements in the SLL are: ')
                sll.display()
            case 8:
                sll.size()
            case 9:
                value = int(input('Enter the value of the node to be searched: '))
                sll.search(value)
            case 10:
                print('Exiting...')
                break
            case _:
                print('Invalid Choice!!!')

    except ValueError:
        print('Please enter valid Choice from 1 to 10')








