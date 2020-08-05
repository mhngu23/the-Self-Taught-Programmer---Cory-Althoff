class Queue:
   def __init__(self):
       self.items = []


   def is_empty(self):
       return self.items == []


   def enqueue(self, item):
       self.items.insert(0, item)
       print(self.items)


   def dequeue(self):
       return self.items.pop()


   def size(self):
       return len(self.items)

queue = Queue()
for i in range(5):
    queue.enqueue(i)

