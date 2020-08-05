def convert_float(x):
    return float(x)
try:
    x = input("Please input numbers: " )
    print(convert_float(x))
except ValueError:
    print("could not convert the string to float")

