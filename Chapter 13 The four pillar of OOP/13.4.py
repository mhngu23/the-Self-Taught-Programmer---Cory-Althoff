class Horse():
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider
        print("""{} is owned by {}""".format(self.name,self.rider.name))
class Rider():
    def __init__(self,name):
        self.name = name

mick = Rider("Mick Jagger")
stan = Horse("Stanley",mick)

