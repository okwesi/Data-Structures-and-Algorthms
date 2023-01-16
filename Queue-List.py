
class Queue:
    def __init__(self):
       self.queue = []
        
    
    def enqueue(self, data):
        self.queue.append(data)
           
            
    def dequeue(self):
       if len(self.queue) >= 1:
            self.queue.pop(0)
    
    def printQueue(self):
        print(self.queue)
   
queue = Queue()
queue.enqueue(34)
queue.enqueue(45)
queue.enqueue(34)
queue.enqueue(428)
queue.printQueue()
queue.dequeue()
queue.dequeue()
queue.printQueue()
queue.enqueue([45,5,7,9])
queue.printQueue()
queue.enqueue(["pass", "Fail", "yes"])
queue.printQueue()
            
