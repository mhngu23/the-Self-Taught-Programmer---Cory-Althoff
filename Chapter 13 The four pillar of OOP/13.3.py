class Shape:
    def what_am_I(self):
        return print("I am a shape")
        
class Regtangular(Shape):
    def __init__(self,a,b):
        self.length = a
        self.width = b
    def calculate_perimeter(self):
        return 2*self.length+2*self.width

class Square(Shape):
    def __init__(self,a):
        self.length = a
    def calculate_perimeter(self):
        return 4*self.length
    def change_size(self,b):
        self.length = self.length - b
        return self.length



reg1 = Regtangular(1,2)
sqr1 = Square(4)
print(reg1.calculate_perimeter())
print(sqr1.calculate_perimeter())
print(sqr1.change_size(1))
print(reg1.what_am_I())
        
        
