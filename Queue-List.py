
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
   
