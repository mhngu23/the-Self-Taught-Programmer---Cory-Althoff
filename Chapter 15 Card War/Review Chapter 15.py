from random import shuffle
class Card:
    suits = ["spades",
             "heart",
             "diamond",
             "club"]
    
    values = ["None","None","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]   #the 2 None is to match the index with the card value
    
    def __init__(self,v,s):
        self.value = v
        self.suit = s
        
    def __lt__(self,c2):    #this is self < c2 case
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
            return False
        
    def __gt__(self,c2):    #this is self > c2 case
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
            return False

    def __repr__(self):     #this function is to access the suits and value of the Card class
        print1 = Card.values[self.value] + " of " + Card.suits[self.suit]
        return print1

#card1 = Card(11,2)
#card2 = Card(11,2)
#print(card1 > card2)
#print(card1)
#print(card2)

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(2,15):
            for j in range(0,4):        
                self.deck.append(Card(i,j))
                shuffle(self.deck)

    def rm_card(self):
        if len(self.deck) == 0:
            return
        else:
            return self.deck.pop()     #to remove the last card that was drawn from the deck

#Deck()

class Player():
    def __init__(self,name):
       self.wins = 0
       self.card = None
       self.name = name
        
      

class War:
    #dir(random)
    def __init__(self):
        player1 = str(input("Player 1 please input your name: "))
        player2 = str(input("Player 2 please input your name: "))
        self.deck = Deck()
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        print(self.deck)

    #def draw(self):
        #return print("{} has drawn {}, {} has drawn {}".format(p1n,p2n,p1c,p2c))
        
    def this_is_war(self):
        cards = self.deck
        print("Begining War")
        while len(cards) >= 2:
            m = input("Press q to quit the game")
            if m == "q":
                break
            p1n = self.player1.name
            p2n = self.player2.name
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            if p1c > p2c:
                print("{} has win this round".format(p1n))
            else:
                print("{} has win this round".format(p2n))
         
        
war = War()
war.this_is_war()

