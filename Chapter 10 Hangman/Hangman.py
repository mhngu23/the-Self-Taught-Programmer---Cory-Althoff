class Hangman:
    def main_function(self,word):
        self.word = []
        for i in range(len(word)):
            self.word.append(word[i])
        body = [" ________  ",
                "|       |  ",
                "|       0  ",
                "|      \|/ ",
                "|       |  ",
                "|      / \ "]

        print("Welcome to Hangman")

        hiddenword = []
        for i in range(len(self.word)):           
            a = "__"
            hiddenword.append(a)
        print(hiddenword)

        wrong = 0        
        while wrong < len(body):
            character = str(input("Please guess a character: "))
            if character in self.word:
                assign_index = self.word.index(character) #this is how to get the index 
                self.word[assign_index] = "$"
                hiddenword[assign_index] = character
                #print(self.word)
                print(hiddenword)
                if "__" not in hiddenword:
                    print("You win the game")
                    break
            else:
                print("You have guessed a wrong character \nPlease guess again")
                wrong += 1
                print("\n".join(body[0:wrong]))
                if wrong >= len(body):
                    print("You have lose the game")
    
        
hangman = Hangman()
import random
animal = ["Tiger","Lion","Elephant","Dog","Cat"]
r = random.choice(animal)
hangman.main_function(r)
       
    
           
        
            
        

