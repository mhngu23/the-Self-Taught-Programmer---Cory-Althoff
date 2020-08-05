def Sequential_Search(lis, n):
    found = False
    for i in lis:
       if i == n:
           found = True
           break
    return found

n = (input("Please input an number "))
list1 = range(1, 100)
list2 = ["1","2","3"]
ss = Sequential_Search(list1,n)
print(ss)
ss2 = Sequential_Search(list2,n)
print(ss2)

