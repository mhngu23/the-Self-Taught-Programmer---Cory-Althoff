class Circle:
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        import math
        #print(dir(math))
        self.area = math.pi*(self.radius**2)
        #self.area = math.pi()
        return print((self.area))
circle = Circle(3)
circle.calculate_area(
