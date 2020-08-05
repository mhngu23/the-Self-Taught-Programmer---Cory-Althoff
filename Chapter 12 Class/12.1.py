class Apple:
    def __init__(self,color,date):
        self.color = color
        self.date = date
        print([self.color,self.date])

apple = Apple("red","today")
print(apple)
