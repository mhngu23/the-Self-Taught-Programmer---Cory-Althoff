def f(x):
    x = str(x)
    if x == str(x):
        print("this is a string")
    else:
        print("this is not a string")
    return x
x = input("please input a string: ")
f(x)
print(x)
