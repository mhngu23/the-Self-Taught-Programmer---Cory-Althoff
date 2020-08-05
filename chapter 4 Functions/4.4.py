def divide_two(a):
    """
    return a/2
    :param a:int
    """
    return a/2

def multy_four(a):
    """
    return a*4
    :param a:int
    """
    return a*4

try:
    a = input("Please enter a number: ")
    a = int(a)
    result1 = divide_two(a)
    print("this is result of part 1: ", result1)
    result2 = multy_four(result1)
    print("this is result of part 2: ", result2)
except ValueError:
    print("this is not a number")

