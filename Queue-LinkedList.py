#Representation of Queue in first in first out principle



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
            
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
           
            
    def dequeue(self):
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
            
            

queue = Queue()
queue.enqueue(34)
queue.enqueue(45)
queue.enqueue(34)
queue.enqueue(428)
queue.printStack()
queue.dequeue()
queue.dequeue()
queue.printStack()
queue.enqueue([45,5,7,9])
queue.printStack()
queue.enqueue(["pass", "Fail", "yes"])
queue.printStack()
            
