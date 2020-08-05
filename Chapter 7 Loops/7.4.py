import random
randomlist = []
for i in range(0,30):
    n = random.randint(1,30)
    randomlist.append(n)
    print(randomlist)
print("Type q to quit")
while True:
    b = input("Guess a number on the list: ")
    if b == "q":
            break
    elif int(b) in randomlist:
        print("You have guess correctly")
    elif int(b) not in randomlist:
        print("Your guess is incorrect:") 
