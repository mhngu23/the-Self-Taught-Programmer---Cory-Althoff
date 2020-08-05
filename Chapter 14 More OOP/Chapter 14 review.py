class Square():
    square_list = []

    def __init__(self,side):
        self.side = side
        self.square_list.append(self.side)

    def print_side(self):
        print("The side of the square is {} by {}".format(self.side,self.side))


s1 = Square(2)
s2 = Square(3)

print(Square.square_list)
s1.print_side()
