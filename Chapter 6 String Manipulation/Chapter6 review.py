class Chapter6_review:
    #def __init__(self)

    def print_String(self,string1): #learn how to print String
        self.string = string1
        i = 0
        for i in range (0,len(self.string)):
            print(self.string[i])
            i+=1

    def insert_String(self,input1,input2): #learn how to use format
        self.input1 = input1
        self.input2 = input2
        print("Yesterday I wrote a {}. I sent it to {}".format(input1,input2))

    def capitalize_first_letter(self,input3):
        """this function capitalize all none English words
            :input3: is the string that you want to make grammaly correct"""
        import enchant #this is online Enlsih dictionary pyEnchant
        self.input3 = input3
        split1 = self.input3.split(" ") #separate the string into list
        d = enchant.Dict("en_US") #call out the English dictionary
        for i in range(0,len(split1)):
            if d.check(str(split1[i])) == False: #if the word not in the dict then caplocks
                a = (str(split1[i]).capitalize())
                split1[i] = a
                i+=1
            else:
                continue
           
        join1 = (" ".join(split1)) #create the new list
        print(join1)

    def list_to_string(self,input4): #split a list into a string
        self.input4 = input4
        print(self.input4.split("?"))

    def replace_a_string(self,input5):
        self.input5 = input5
        print(self.input5.replace("s","$"))

    def find_first_index(self,input6):
        self.input6 = input6
        print(self.input6.index("m"))

    def turn_Into_String(self,input7):
        self.input7 = str(input7)
        print(self.input7)

    def concatenation_multiplication(self,input8,input9):
        self.input9 = (input9 + " ") *3
        self.input8 = input8 + " " + input8 + " " + input8
        print(self.input8,self.input9)

    def splicing(self,input10):
        self.input10 = input10[0:33]
        print(self.input10)
        
        

chapter6 = Chapter6_review()
#chapter6.print_String("Camus")
#chapter6.insert_String(str(input("Please enter something ")),str(input("Please enter another ")))
#chapter6.capitalize_first_letter("nhi lam was born in 2000")
#chapter6.list_to_string("Where now? Who now? When now?")
#chapter6.replace_a_string("A screaming comes across the sky.")
#chapter6.find_first_index("Hemingway")
#chapter6.turn_Into_String("He said: \"Hello\"")
#chapter6.concatenation_multiplication("three","three")
chapter6.splicing("It was a bright cold day in April, and the clocks were striking thirteen")
