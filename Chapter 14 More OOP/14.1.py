#14.1 and 14.2
class Square:
    square_list = []

    def __init__(self,s):
        self.side = s
        self.square_list.append(self.side)

    def print_size(self):
        print("""{} by {}""".format(self.side,self.side))


s1 = Square(20)

print(Square.square_list)
s1.print_size()
