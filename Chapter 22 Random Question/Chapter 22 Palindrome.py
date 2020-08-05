class Palindrome:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        return self.items.append(item)
        
        
    def pop(self):
        return self.items.pop()
    
    
item = "ABC"
item2 = "CBA"
palindrome = Palindrome()
for c in item2:
    palindrome.push(c)
#print(palindrome.items)

reverse = ""        
for i in range(0,len(palindrome.items)):
    reverse += palindrome.pop()
print(reverse)

def Checking_Palindrome(a,b):
        is_Palindrome = False
        if str(a) == str(b):
            is_Palindrome = True
        return is_Palindrome

print(Checking_Palindrome(item,reverse))



