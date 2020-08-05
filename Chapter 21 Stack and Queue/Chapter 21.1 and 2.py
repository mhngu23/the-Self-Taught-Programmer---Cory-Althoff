class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
        return self.items
    def pop(self):
        return self.items.pop()
    def peek(self):
        last = len(self.items)-1
        return self.items(last)
    def size(self):
        return len(self.items)
stack = Stack()
stack1 = Stack()

list1 = [1,2,3,4,5]
list2 = []
for item in list1:
    stack1.push(item)
for a in "yesterday":
    stack.push(a) 
reverse = ""
for i in range(len(stack.items)):
    reverse += stack.pop()
print(reverse)

for b in range(len(stack1.items)):
    list2.append(stack1.pop())
print(list2)
