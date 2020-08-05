class review_Chapter_7:
    def for_Loop_To_Print(self,input1):
        self.input1 = input1
        for i in range(len(self.input1)):
            print(self.input1[i])
            print(i)
        i = 0
        while i<len(self.input1):
            print(self.input1[i])
            i +=1
            
    def print_25_50(self):
        i = 25
        while i<=50:
            print(i)
            i +=1
            
    def guess_a_number(self):
        import random
        the_list = []
        for i in range(0,100):
            n = random.randint(0,100)
            the_list.append(n)    
        #print(the_list)
        print("Type q to quit")
        i=5
        while i < 10:
            self.input = input("Please guess a number: ")
            if self.input == "q":
                print("you have quit the game")
                break
            else: 
                if int(self.input) in the_list:
                    print("Your guess is correct")
                else:
                    print("your guess is incorrect")

    def multiply_Two_List(self):
        list1 = [8,19,148,4]
        list2 = [9,1,33,83]
        list3 = []
        for i in list1:
            for j in list2:
                a = i*j
                list3.append(a)
        print(list3)
                
        
                
           
                    

chapter7 = review_Chapter_7()
#chapter7.for_Loop_To_Print(["the Walking Dead", "Entourage","The Scopranos", "The Vampire Diaries"])
#chapter7.print_25_50()
#chapter7.guess_a_number()
chapter7.multiply_Two_List()
