class Shape:
    def what_am_i(self):
        return print("I am a shape")
    
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def calculate_perimeter(self):
        self.area = self.side*4
        return print(self.area)
    def change_size(self):
        self.new_side = self.side + 2
        #self.new_perimeter = Square(self.new_side)
        print(self.new_side)
        #self.new_perimeter.calculate_perimeter()
        
class Regtangle(Shape):
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2
    def calculate_perimeter(self):
        self.area = self.side1 * 2 + self.side2 * 2
        return print(self.area)

class Horse():
    def __init__(self,name,color,owner):
        self.name = name
        self.color = color
        self.owner = owner
    def print_out(self):
        print("The owner of {} is {}".format(self.name,self.owner))

class Owner():
    def __init__(self,name):
        self.name = name
    def return_owner_name(self):
        return self.name
        #return print("The name of the owner is {}".format(self.name))


square = Square(2)
regtangle = Regtangle(2,3)
#square.calculate_perimeter()
#square.change_size()
#regtangle.calculate_perimeter()
#regtangle.what_am_i()

owner = Owner("LeeMinHo")
horse = Horse("white horse","white",owner.return_owner_name())
horse.print_out()


