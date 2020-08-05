class Hexagon:
    def __init__(self,s):
        self.side = s
    def perimeter(self,s):
        self.perimeter=6*self.side
        self.perimeter = 6*s
        return self.perimeter
Hexagon1=Hexagon(3)
print(Hexagon1.perimeter(4))
