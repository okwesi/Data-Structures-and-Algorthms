class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class Stack:
    def __init__(self):
        self.head = None
        
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
            
    
    def push(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            
    def pop(self):
        if self.head:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
        else:
            return None
    
    def printStack(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()
            
            

stack = Stack()
stack.push(34)
stack.push(45)
stack.push(34)
stack.push(428)
stack.printStack()
stack.pop()
stack.printStack()
stack.push([45,5,7,9])
stack.printStack()
stack.push(["pass", "Fail", "yes"])
stack.printStack()
