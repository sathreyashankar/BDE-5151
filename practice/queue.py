class Queue:
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)
        print('Data Inserted: ', data)
        self.display()
        return

    def pop(self):
        print('Element Deleted: ', self.queue[0])
        self.queue.pop(0)
        self.display()
        return

    def peek(self):
        if len(self.queue == 0):
            print('Queue Empty! No Top Element to Display!')
            return
        print('Top\(or First\) Element in the Queue: ', self.queue[-1])
        return

    def size(self):
        print('Length of the current Queue is: ', self.queue)

    def display(self):
        if len(self.queue) == 0:
            print('Queue Empty, nothing to display!')
            return
        print('Elements in Queue are: \n')
        print(self.queue)
        return

    
q = Queue()

flag = True
x = 0
choice = 0
while flag:
    print('\nChoose 1 for Insertion into the Queue: ')
    print('\nChoose 2 for Deletion from the front end of the queue: ')
    print('\nChoose 3 for printing the front most element of the queue without deleting it: ')
    print('\nChoose 4 for checking the length of the queue currently: ')
    print('\nChoose 5 to display the contents in the queue: ')
    print('\nChoose 6 or any other key to exit: ')

    choice = int(input('Enter your choice: '))

    match choice:
        case 1:
            data = int(input('Enter the element to be pushed into the queue: '))
            q.push(data)
        case 2:
            q.pop()
        case 3:
            q.peek()
        case 4:
            q.size()
        case 5:
            q.display()
        case 6:
            print('Exiting ... ')
            break
        case _:
            print('Invalid Choise! Exiting ... ')
            break
