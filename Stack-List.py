


class Stack:
    def __init__(self):
       self.queue = []
        
    
    def push(self, data):
        self.queue.append(data)
           
            
    def pop(self):
       if len(self.queue) >= 1:
            self.queue.pop()
    
    def printStack(self):
        print(self.queue)
            
            

stack = Stack()
stack.push(34)
stack.push(45)
stack.push(34)
stack.push(428)
stack.printStack()
stack.pop()
stack.pop()
stack.printStack()
stack.push([45,5,7,9])
stack.printStack()
stack.push(["pass", "Fail", "yes"])
stack.printStack()
stack.pop()
stack.printStack()
           
