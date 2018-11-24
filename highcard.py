import random #For Shuffle
import time #Creates delays in the Menu

from classes import *

# Global Variables

p1_score = 0
p2_score = 0
menu_options = ["Play", "See Scoreboard", "End", "1", "2", "3"]
deck = Deck(1) # Creates a new deck from the Deck class in cards.py


def scoreboard():
    """Shows the Scoreboard """
    global p1_score
    global p2_score
    return "\nPlayer One Score: {}\nPlayer Two Score: {}".format(p1_score,p2_score)


def compare_values(card1, card2):
    """Computes the .value between two cards and returns both values """
    value1 = card1.value()
    value2 = card2.value()
    return value1, value2


def pick():
    """Each player picks a card at random, removes the cards from deck, and decides the winner via compare_values()"""
    player_one_choice = random.choice(deck.cards)
    deck.kill(player_one_choice)
    player_two_choice = random.choice(deck.cards)
    deck.kill(player_two_choice)
    scores = compare_values(player_one_choice, player_two_choice)
    if scores[0] > scores[1]:
        winner = "Player One Wins!"
        global p1_score
        p1_score += 1
    elif scores[0] < scores[1]:
        winner = "Player Two Wins!"
        global p2_score
        p2_score += 1
    else:
        winner = "It's a Draw!"
    return player_one_choice, player_two_choice, scores, winner


def game_menu():
    """Main game menu, using time to create delays, loops infinitely until 'End' is chosen"""
    while True:
        print("\nWelcome to High Card!\n\n---\n")
        time.sleep(1.5)
        print("Please select an option from the menu:\n ")
        print("1) Play")
        print("2) See Scoreboard")
        print("3) End\n\n---\n")
        selection = input("What would you like to do?: ")
        if selection not in menu_options:
            print("Please Enter a Valid Option")
        elif selection == "Play" or selection == "1":
            print("\n...shuffling deck...\n")
            time.sleep(1)
            p1_pick, p2_pick, scores, winner = pick()
            print("Player One Draws...\n")
            time.sleep(2)
            print("...The {}.\n".format(p1_pick))
            time.sleep(2)
            print("Player Two Draws...\n")
            time.sleep(2)
            print("...The {}.\n".format(p2_pick))
            time.sleep(3)
            print("---\n")
            time.sleep(.5)
            print("{}".format(winner))
            print("\n---")
            time.sleep(2)
            print(scoreboard())
            print("\n---")
            time.sleep(2)
        elif selection == "See Scoreboard" or selection == "2":
            print(scoreboard())
            time.sleep(2)
        elif selection == "End" or selection == "3":
            print("Thank You For Playing!")
            break


game_menu()
