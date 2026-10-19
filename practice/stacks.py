class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow! No elements to delete or pop from the stack!")
            return
        return self.stack.pop()

    def size(self):
        print('Length of the current stack: ', len(self.stack))

    def peek(self):
        if len(self.stack) == 0:
            print('Stack Empty!')
            return None
        else:
            print('Top element: ', self.stack[-1])

    def display(self):
        print(self.stack)


s = Stack()

flag = True
x = 0
choice = 0
while flag:
    print('\nChoose 1 for Insertion into the stack from the top: ')
    print('\nChoose 2 for Deletion from the top of the stack: ')
    print('\nChoose 3 for printing the top element of the stack without deleting it: ')
    print('\nChoose 4 for checking the length of the stack currently: ')
    print('\nChoose 5 to display the contents in the stack: ')
    print('\nChoose 6 or any other key to exit: ')

    choice = int(input('Enter your choice: '))

    match choice:
        case 1:
            data = int(input('Enter the element to be pushed into the stack: '))
            s.push(data)
        case 2:
            s.pop()
        case 3:
            s.peek()
        case 4:
            s.size()
        case 5:
            s.display()
        case 6:
            print('Exiting ... ')
            break
        case _:
            print('Invalid Choise! Exiting ... ')
            break


           
        
        
        

    

    