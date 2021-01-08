#Luke Rowberry
#1/6/2021
#Blackjack game
import playing_cards as pc
import game_functions as gf

class BJ_Card(pc.Pos_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.faceup:
            v = BJ_Card.RANKS.index((self.rank))+1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(pc.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.add(BJ_Card(rank,suit))

class BJ_Hand(pc.Hand):
    def __init__(self,name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        print("############################################")
        for card in self.cards:
            print(card)
        rep = "############################################"
        rep += "\n "+self.name
        rep += "\n "+self.total
        return rep

    @property
    def total(self):
        #if card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        #add up card values, Aces = 1
        t = 0
        for card in self.cards:
            t += card.value
        #determine is Ace in hand
        has_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                has_ace = True
        #if hand contains Ace and if hand value low enough, treat as 11
        if has_ace and t <= 11:
            t += 10
        return t
    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):

    def bust(self):
        print(self.name, "busts.")
        self.lose()
    def lose(self):
        print(self.name, "loses.")
    def win(self):
        print(self.name, "wins.")
    def push(self):
        print(self.name, "pushes.")
    def is_hitting(self):
        response = gf.ask_yes_no("\n"+self.name+", do yuo want to hit? (Y/N):")
        return response == "y"

class BJ_Dealer(BJ_Hand):

    def is_hitting(self):
        return self.total < 17 
    def bust(self):
        print(self.name, "busts.")
    def flip_first_card(self):
        self.cards[0].flip()

class Game(object):
    def __init__(self,names):
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.dealer = BJ_Dealer("Dealer Tim")
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

        
        
        
    
            

#testing area
deck = BJ_Deck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)
