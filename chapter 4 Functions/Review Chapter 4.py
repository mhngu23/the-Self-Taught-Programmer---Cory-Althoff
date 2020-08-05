class chapter_4_Functions:
    """Review Chapter 4 Excercise
        :number: int
        :string: str
        :string2: input but number string only"""
    def __init__(self,number,string,string2):
        self.number = number
        self.string = string
        self.string2 = string2
        
    def square(self):
        return print(self.number ** 2)

    def print_String(self):
        return print(self.string)

    def divide_2(self):
        return (self.number/2)

    def multiply_4(self,number2):
        return print(number2*4)

    def float(self):
        try:
            a = float(self.string2) #dont use variable defined in an exception 
        except(ValueError):
            print("Input must be a number")

chapter4 = chapter_4_Functions(2,"this is a string","abc")

chapter4.square()
chapter4.print_String()
a = chapter4.divide_2()
print(a)
chapter4.multiply_4(a)
chapter4.float()    
    

    
    
