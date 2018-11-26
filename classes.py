import random
import sys
import time


def order_drink():
    print("Drink Menu:\n")
    print("1)Whiskey, neat")
    print("2)Gatorade and Tequila")
    print("3)Vodka Redbull")
    print("4)Bacardi & Cola, do it.")
    print("5)Water")
    print("6)Moscow Mule")
    drink = input("\nWhat would you like to order? ")
    print("\nGood choice, enjoy!\n")
    return "Good choice, enjoy!"

def show_down(dealer,player,bet,bankroll):

    if dealer > 21:
        print("The Dealer Busts!\n")
        time.sleep(2)
        print("You win {} chips!\n".format(bet))
        print("---")
        time.sleep(2)
        return "win"

    if player > dealer:
        print("You have {}\n".format(player))
        time.sleep(2)
        print("You win {} chips!\n".format(bet))
        print("---")
        time.sleep(2)
        return "win"

    elif player < dealer:
        print("You have {}\n".format(player))
        time.sleep(2)
        print("You lose {} chips!\n".format(bet))
        print("---")
        time.sleep(2)
        return "lose"

    else:
        print("You have {}\n".format(player))
        time.sleep(2)
        print("You and The Dealer Pushed!\n")
        print("---")
        time.sleep(2)
        return "push"


class Card:

    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __eq__(self, other):
        return str(self) == str(other)

    def shorthand(self):
        if self.rank != "10":
            return self.rank[0] + self.suit[0]
        else:
            return "10" + self.suit[0]

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
        if self.rank == "Jack":
            return 10
        elif self.rank == "Queen":
            return 10
        elif self.rank == "King":
            return 10
        elif self.rank == "Ace":
            return 1
        else:
            return int(self.rank)

    def color(self):
        if self.suit == "Diamond" or self.suit == "Hearts":
            return "Red"
        else:
            return "Black"


class Deck:

    discard_pile = []
    up_cards = []

    def __init__(self, *args):
        cards = []
        for i in range(*args):
            for rank in Card.RANKS:
                for suit in Card.SUITS:
                    c = Card(suit=suit, rank=rank)
                    cards.append(c)
        if cards is None:
            cards = []
            for rank in Card.RANKS:
                for suit in Card.SUITS:
                    c = Card(suit=suit, rank=rank)
                    cards.append(c)
        else:
            cards = list(cards)
        self.cards = cards

    def __add__(self, other):
        return Deck(self.cards + other.cards)

    def insert_cut_card(self):
        cut_card = Card("Card", "Cut")
        back_third = len(self.cards)//3*2
        random_index = random.randint(back_third,len(self.cards))

        return self.cards.insert(random_index, cut_card)

    def show_cut_card(self):
        return "The cut card is in the {} position of the deck".format(self.show_cards().index(Card("Card","Cut")))

    def show_cards(self):
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

    def deal(self, amount = 1):
        return self.cards.pop(0)

    def __repr__(self):
        return "Deck of {} cards".format(len(self.cards))


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.bankroll = 0
        self.bet = 0
        self.play = True
        self.insurance = 0
        self.turn = 0

    def play_menu(self):
        result_list = [1, 2, 3, 4, 5]
        print("Please Select an Option: \n")
        print("1)Deal")
        print("2)Chip Count")
        print("3)Buy More Chips")
        print("4)Buy a Drink")
        print("5)Quit")
        while True:
            try:
                result = int(input("---> "))
                if result not in result_list:
                    print("Oops!  That was not a valid number.  Try again...")
                else:
                    break
            except ValueError:
                print("Oops!  That was not a valid number.  Try again...")
        while result:
            if result == 1:
                return 1
            elif result == 2:
                print("You have {} chips.".format(self.bankroll))
                print("---")
                result = self.play_menu()
            elif result == 3:
                print(self.buy_more_chips())
                result = self.play_menu()
            elif result == 4:
                order_drink()
                result = self.play_menu()
            elif result == 5:
                print("Thanks for Playing, {}!".format(self.name))
                sys.exit()

    def bj_menu(self):
        print("Please Select an Option:\n ")
        print("1)Hit")
        print("2)Stand")
        print("3)Double Down")
        #print("4)Split") IMPLEMENT NEXT
        #print("5)Surrender")
        x = int(input("---> "))
        return x

    def play_card(self, x):
        if x not in self.hand:
            print("{} not in hand!".format((x)))
        else:
            Deck.up_cards.append(x)
            return self.hand.remove(x)

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    def show_hand(self):
        myList = ', '.join(map(str, self.hand))
        return "You have the {}\n".format(myList)

    def discard(self, x):
        if x not in self.hand:
            print("{} not in hand!".format(x))
        else:
            Deck.discard_pile.append(x)
            return self.hand.remove(x)

    def hand_value(self):
        hard_value = 10
        soft_value = 0
        ace_in_hand = False
        for card in self.hand:
            hard_value += card.bj_value()
            soft_value += card.bj_value()
        for card in self.hand:
            if card.rank == "Ace":
                ace_in_hand = True
        if ace_in_hand:
            if hard_value <= 21:
                return hard_value
            else:
                return soft_value
        else:
            return soft_value

    def hand_check(self):
        if self.hand_value() == 21:
            print("You Have Blackjack!\n")
            time.sleep(2)
            payout = (self.bet * 3/2)
            self.bankroll += (self.bet * 3/2)
            print("You won {}!".format(payout))
            time.sleep(2)
            self.bet = 0
            print("---")
            return "Blackjack"
        elif self.hand_value() > 21:
            print("You Busted with {}!\n". format(self.hand_value()))
            time.sleep(2)
            print("You lost {} chips!".format(self.bet))
            time.sleep(2)
            self.bankroll -= self.bet
            self.bet = 0
            print("---")
            return "Bust"
        else:
            return "Valid"

    def chips(self):
        print("How many chips would you like to start with?")
        while True:
            try:
                chip_count = int(input("---> "))
                if chip_count < 0 or chip_count == 0:
                    print("Oops!  That was not a valid number.  Try again...")
                else:
                    break
            except ValueError:
                print("Oops!  That was not a valid number.  Try again...")
        self.bankroll = chip_count
        if self.bankroll >= 10000:
            print("\nYou've been moved to the high roller table!\n")
            time.sleep(1.5)
        else:
            print("\n...Changing {}!\n\n---".format(self.bankroll))
            time.sleep(1.5)
        self.bankroll = chip_count
        return self.bankroll

    def buy_more_chips(self):
        print("How many more chips would you like to purchase?: ")
        while True:
            try:
                chip_count = int(input("---> "))
                if chip_count < 0 or chip_count == 0:
                    print("Oops!  That was not a valid number.  Try again...")
                else:
                    break
            except ValueError:
                print("Oops!  That was not a valid number.  Try again...")
        self.bankroll = self.bankroll + chip_count
        return "You now have {} chips!\n---".format(self.bankroll)

    def take_bet(self):
        while True:
            try:
                bet = int(input("How much would you like to wager? "))
                self.bet = bet
                if bet > self.bankroll:
                    print("\nYou don't have enough chips.\n")
                elif bet < 0 or bet == 0:
                    print("Oops! You cannot bet less than 0. Try again...\n")
                else:
                    break
            except ValueError:
                print("Oops! That was not a valid number. Try again...\n")
        return bet

    def __repr__(self):
        return "Name: {}".format(self.name)


class Dealer(Player):

    insurance_flag = False

    def dealer_hand_check(self):
        if self.hand_value() == 21:
            time.sleep(1)
            return "Blackjack"

    def show_upcard(self):
        if self.hand[0].rank == "Ace":
            self.insurance_flag = True
            return "The Dealer shows a {}".format(self.hand[0])
        else:
            return "The Dealer shows a {}".format(self.hand[0])

    def dealer_show_hand(self):
        myList = ', '.join(map(str, self.hand))
        return "The Dealer has the {}\n".format(myList)


