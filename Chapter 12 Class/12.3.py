class Triangle():
    def __init__(self,h,b):
        self.height = h
        self.base = b

    def area(self):
        return self.height*self.base/2

Triangle1 = Triangle(2,3)
print(Triangle1.area())
