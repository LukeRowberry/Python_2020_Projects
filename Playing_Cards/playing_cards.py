#Luke Rowberry
#12/17/2020
#playing cards class
import random
class Card(object):
    RANKS = ["A","2","3","4","5","6","7",
             "8","9","10","J","Q","K"]
    SUITS = ["♠","♣","♦","♥"]

    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rep = str.format("""
        +----------+
        | {1}{0:>2}      |
        |          |
        |          |
        |          |
        |          |
        |      {0:2}{1} |  
        +----------+
        
        """,self.rank,self.suit)
        return rep

class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)
        else:
            rep = "<EMPTY>"
        return rep
    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def deal(self,hands,per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Out of Cards - Clearing Hands - Reshuffling")
                    self.clear()
                    self.populate()
                    self.shuffle()
                    for hand in hands:
                        hand.clear()
                    self.deal()

class Pos_Card(Card):
    def __init__(self,rank,suit):
        super(Pos_Card, self).__init__(rank,suit)
        self.faceup = True

    def flip(self):
        self.faceup = not self.faceup

    def __str__(self):
        if self.faceup:
            rep = super(Pos_Card, self).__str__()
        else:
            rep = """
        +----------+
        |##########|
        |##########|
        |##########|
        |##########|
        |##########|
        |##########|  
        +----------+
                """
        return rep

#card = Pos_Card("A","♠")
#print(card)
#card.flip()
#print(card)

# deck = Deck()
# deck.populate()
# deck.shuffle()
#
# player1 = Hand()
# player2 = Hand()
# river = Hand()
# players = [player1,player2]
# for i in range(2):
#     deck.deal(players,1)
#     deck.deal([river],1)
#
#
# print(river)
# print(player1)
# input("Player1 Bet")
# print(player2)
# input("Player2 Bet")
#
# for i in range(3):
#     deck.deal([river],1)
#     print(river)
#     print("Player1")
#     print(player1)
#     input("Player1 Bet")
#     print("Player2")
#     print(player2)
#     input("Player2 Bet")

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the ENTER key to exit.")

