class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        #print(len(self.items))
        return len(self.items)

    def peek(self):
        i = len(self.items)-1
        return self.items[i]

stack = Stack()
string = "Yesterday"

for i in range(len(string)):
    stack.push(string[i])
#stack.size()

reverse = ""
for i in range(stack.size()):
    reverse += stack.pop()

print(reverse)

