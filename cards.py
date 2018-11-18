import random


class Card:

    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)

    def value(self):
        if self.rank == "Jack":
            return 11
        elif self.rank == "Queen":
            return 12
        elif self.rank == "King":
            return 13
        elif self.rank == "Ace":
            return 14
        else:
            return int(self.rank)

    def is_face(self):
        if self.rank == "Jack":
            return True
        elif self.rank == "Queen":
            return True
        elif self.rank == "King":
            return True
        else:
            return False

    def bj_value(self):
        pass

    def color(self):
        if self.suit == "Diamond" or self.suit == "Hearts":
            return "Red"
        else:
            return "Black"


class Deck:
    def __init__(self):
        self.cards = []
        self.discard_pile = []
        self.up_cards = []
        for rank in Card.RANKS:  # ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
            for suit in Card.SUITS:  # ["Hearts", "Clubs", "Diamonds", "Spades"]
                c = Card(suit=suit, rank=rank)
                self.cards.append(c)

    def showcards(self):
        return self.cards

    def discard(self, x):
        for i in range(x):
            card = self.cards.pop(0)
            self.discard_pile.append(card)
        return self.cards

    def kill(self, y):
        return self.cards.remove(y)

    def shuffle(self):
        return random.shuffle(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(len(self.cards))



deck = Deck()

x = random.choice(deck.cards)
y = random.choice(deck.cards)

print(type(x))

def compare_values(card1, card2):
    value1 = card1.value()
    value2 = card2.value()
    return value1, value2

#print(compare_values("Jack of Hearts", "2 of Diamonds"))




print(compare_values(x,y))









