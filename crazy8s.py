#How do you play Crazy Eights?
'''
ASSUME YOU ARE DOING A TWO PLAYER GAME

Eight cards are dealt to each player (or seven in a two-player game).
The remaining cards of the deck are placed face down at the center of the table.
The top card is then turned face up to start the game.

Players discard by matching rank or suit with the top card of the discard pile,
starting with the player left of the dealer.
If a player is unable to match the rank or suit of the top card of the discard pile
and does not have an 8, they draw cards from the stockpile until they get a playable card.
When a player plays an 8, they must declare the suit that the next player is to play;
that player must then follow the named suit or play another 8.

As an example: Once 6♣ is played the next player:

can play any of the other 6s
can play any of the clubs
can play any 8 (then must declare a suit)
can draw from the stockpile until willing and able to play one of the above
The game ends as soon as one player has emptied their hand.
'''

import random
import time
from random import shuffle

def generate_deck():
    deck = []
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    RANKS = [str(item) for item in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
    for suit in SUITS:
        for rank in RANKS:
            deck.append((rank, suit))
    return deck

# Global Vars
move = True
game_on = False
turn = 0
p1_score = 0
p2_score = 0
p1_hand = []
p2_hand = []
deck = generate_deck()
up_cards = []
menu_options = ["Play", "See Scoreboard", "End", "1", "2", "3"]
game_options = ["Draw Card", "Show Hand", "Show Board", "Play Card","1", "2", "3", "4"]
active_suit = []


def compare_values(card1, card2):
    faces = {"Jack":11,"Queen":12,"King":13,"Ace":14}
    value1 = card1.split()[0]
    value2 = card2.split()[0]
    if value1 in faces:
        value1 = faces[value1]
    if value2 in faces:
        value2 = faces[value2]
    return int(value1), int(value2)


def shuffle_deck():
    global deck
    x = [i for i in deck]
    shuffle(x)
    return x

def coin_flip():
    choices = (1,2)
    flip = random.choice(choices)
    return flip

def change_turn():
    global turn
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1

def moveflag():
    global move
    if move == True:
        move = False
    elif move == False:
        move = True


def scoreboard():
    global p1_score
    global p2_score
    return "\nPlayer One Score: {}\nPlayer Two Score: {}".format(p1_score,p2_score)

def begin_game():
    global p1_hand, p2_hand, deck, up_cards, game_on, turn, active_suit
    game_on = True
    deck = shuffle_deck()
    #time.sleep(1)
    print('\n...dealing cards...')
    for card in range(7):
        p1_card = random.choice(deck)
        deck.remove(p1_card)
        p1_hand.append(p1_card)
    for card in range(7):
        p2_card = random.choice(deck)
        deck.remove(p2_card)
        p2_hand.append(p2_card)
    flip = coin_flip()
    print("\n...shuffling deck...\n")
    #time.sleep(2)
    print("...flipping coin...\n")
    #time.sleep(1)
    if flip == 1:
        print("Player One Goes First!\n")
        turn = 1
    else:
        print("Player Two Goes First!\n")
        turn = 2
    #time.sleep(1)
    up_cards.append(deck.pop(0))
    print("The Up Card is The {}.\n".format(up_cards[0]))
    active_suit = [x[1] for x in up_cards]
    return p1_hand, p2_hand, len(deck), deck[0], turn

def show_hand(player):
    if player == 1:
        print(p1_hand)
        return p1_hand
    elif player == 2:
        print(p2_hand)
        return p2_hand


def shorthand(hand):
    sh = []
    for x,i in hand:
        if x == "10":
            sh.append(''.join((x[0:2], i[0])))
        else:
            sh.append(''.join((x[0], i[0])))
    return sh


def start_menu():
    while True:
        print("\nWelcome to Crazy 8s!\n\n---\n")
        #time.sleep(1.5)
        print("Please select an option from the menu:\n ")
        print("1) Play")
        print("2) See Scoreboard")
        print("3) End\n\n---\n")
        selection = input("What would you like to do?: ")
        if selection not in menu_options:
            print("Please Enter a Valid Option")
        elif selection == "Play" or selection == "1":
            begin_game()
            #time.sleep(2)
            play_menu()
            break
        elif selection == "See Scoreboard" or selection == "2":
            print(scoreboard())
            #time.sleep(2)
        elif selection == "End" or selection == "3":
            print("Thank You For Playing!")
            break

def play_card():
    global p1_hand, p2_hand
    if turn ==1:
        hand = p1_hand
    elif turn ==2:
        hand = p2_hand
    print("\nPlayer {} Here is Your Hand: {} \n".format(turn,hand))
    print("The up card is {}\n".format(up_cards))
    s_hand = shorthand(hand)
    upcard_short = shorthand(up_cards)
    while True:
        card = input("Please Select a Card To Play: ")
        if card in s_hand:
            for x in card:
                print(x)
                print("VALID")
                break

        else:
            print("\nInvalid Entry\n")
    return card

def show_board():
    print("\nPlayer One Has {} cards remaining.\n".format(len(p1_hand)))
    print("Player Two Has {} cards remaining.\n".format(len(p2_hand)))
    print("The Up Card Is {}.\n".format(up_cards[0]))


def play_menu():
    while True:
        print("Game Menu: \n\n---\n".format(turn))
        #time.sleep(1.5)
        print("1) Play Card")
        print("2) Draw Card")
        print("3) Show Hand")
        print("4) Show Board")
        selection = input("\nPlayer {} Select a Move: ".format(turn))
        if selection == "1":
            play_card()
        elif selection == "3":
            show_hand(turn)
            print(p1_hand)
            print(p2_hand)
        elif selection == "4":
            show_board()


start_menu()
