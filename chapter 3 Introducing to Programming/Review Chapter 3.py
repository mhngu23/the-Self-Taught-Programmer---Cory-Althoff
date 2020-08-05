class review_Chapter_3:
    def __init__(self,number1,number2):
        self.n1 = number1
        self.n2 = number2
    def comparison(self):
        if (self.n1) < 10:
            print("Hello")
        else:
            print("Goodbye")
    def remainder(self):
        return print(self.n1 % self.n2)
    def quotient(self):
        return print(self.n1 / self.n2)

a = int(input("Please input a number: "))
b = review_Chapter_3(a,10)
b.comparison()
b.remainder()
b.quotient()
