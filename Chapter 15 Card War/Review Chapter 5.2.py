import random

class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]
    values = ["None","None","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def __init__(self,v,s):
        self.value = v
        self.suit = s

    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
            return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
            return False

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

#card = Card(3,3)

class Deck:
    def __init__(self):
        self.deck = []
        for i  in range(2,14):
            for j in range(0,4):
                v = Card(i,j)
                self.deck.append(v)
        random.shuffle(self.deck)

    def rm_card(self):
        if len(self.deck) == 0:
            return
        return self.deck.pop()
        
#Deck()
        
class Player:
    def __init__(self,name):
        self.won = 0
        self.Card = None
        self.name = name

class War:
    def __init__(self):
        self.deck = Deck()
        name1 = str(input("Please input player 1 name: "))
        name2 = str(input("Please input player 2 name: "))
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def draw(self,p1n,p2n,p1c,p2c):
        print("{} has drawn a {}, {} has drawn a {}".format(p1n,p1c,p2n,p2c))


    def playing_game(self):
        deck = self.deck.deck
        while len(deck)>2:
            p1n = self.p1.name
            p2n = self.p2.name 
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            self.draw(p1n,p2n,p1c,p2c)
            if p1c > p2c:
                self.p1.won += 1
                print("{} has won this round".format(p1n))
            else:
                self.p2.won+=1
                print("{} has won this round".format(p2n))

        win = self.winner(self.p1.won,self.p2.won)
     
        
    def winner(self,p1w,p2w):
        self.p1w = p1w
        self.p2w = p2w
        if self.p1w > self.p2w:
            return print("{} is the final winner".format(self.p1.name))
        elif self.p1w < self.p2w:
            return print("{} is the final winner".format(self.p2.name))
        else:
            return print("it was a tie")        

war = War()
war.playing_game()

        
