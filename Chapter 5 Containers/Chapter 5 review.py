class Chapter5_Review:
    #def __init__(self,question4):
        #self.question4 = question4

    def create_list(self):
        list1 = ["apple",1,1.5]
        return print(list1)

    def create_tuples(self):
        location = ("1239:12356","1245:1235")
        return print(location)

    def create_dictionary(self):
        dictionary = {"height":
                      "175cm",
                      "weight":
                      "62kg"}
        print(dictionary)
        return dictionary

    def asking_question(self,question4):
        self.question4 = a
        input_customers = input("Please input height or weight to find the info: ")
        if input_customers in self.question4:
            return print(self.question4[input_customers])
        else:
            print("this is not in the dictionary")
        


run = Chapter5_Review()
run.create_list()
run.create_tuples()
a = run.create_dictionary()
run.asking_question(a)

