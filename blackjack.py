from classes import *
import time
import sys

#Game Menu


print("Hello! Welcome to Blackjack!\n")
time.sleep(2)
player = Player(str(input("What is your name?: ")))
print("---")
print("Hi {}, Good Luck!\n---".format(player.name))
time.sleep(2)

#Create 8 Decks and the Dealer

deck = Deck(8)
dealer = Dealer("Dickhead")

#Shuffle the 8 Decks

deck.shuffle()

#Insert the cut card at a random index in the final third of the deck

#deck.insert_cut_card() IMPLEMENT NEXT

#Inital Chip Purchase

player.chips()


#Main Game Menu


while player.play:

    start_game = player.play_menu()

    hand_valid = True

    if start_game == 1:
        dealer.hand = []
        player.hand = []

        #Take Bet

        player.take_bet()
        print("---")

        #Deal to Player and Dealer

        print("...Dealing Cards...")
        time.sleep(1.5)
        print("---")
        player.draw(deck)
        dealer.draw(deck)
        player.draw(deck)
        dealer.draw(deck)

        #USE TO TEST HANDS
        #player.hand = [Card("Hearts", "5"), Card("Hearts", "2")]
        #dealer.hand = [Card("Hearts", "5"), Card("Hearts", "King")]

        #Phase 1 - Displaying Dealer and Player Hands

        print(dealer.show_upcard())
        time.sleep(1.5)
        print("\nYou have the {} and the {}".format(player.hand[0], player.hand[1]))
        time.sleep(2)
        print("---")

        while hand_valid:

            #Phase 2 - Check for insurance and Initial BlackJacks and Ties

            if dealer.dealer_hand_check() == "BlackJack":
                if player.hand_value() == 21:
                    print("You Have BlackJack!\n")
                    print("You and the Dealer pushed!\n")
                    time.sleep(2)
                    hand_valid = False
                    break
                elif player.hand_value() != 21:
                    print("You lost {}!\n".format(player.bet))
                    player.bankroll -= player.bet
                    time.sleep(2)
                    hand_valid = False
                    break
            elif player.hand_value() == 21:
                print("You Have BlackJack!\n")
                time.sleep(2)
                print("You Win {} chips!\n".format(player.bet * 3/2))
                time.sleep(3)
                player.bankroll += player.bet * 3/2
                break
            else:
                print("**Implement insurance check**\n")
                #dealer.check_insurance() IMPLEMENT NEXT

            # Phase 3 - Player Actions

            bj_menu = player.bj_menu()

            #1)Hit

            if bj_menu == 1:
                player.draw(deck)
                print("You hit the {}\n".format(player.hand[-1]))
                time.sleep(2)
                print(player.show_hand())
                time.sleep(2)
                print(dealer.show_upcard())
                time.sleep(2)
                print("---")
                if player.hand_check() == "Bust":
                    break
                elif player.hand_check() == "Blackjack":
                    print("You Have BlackJack!\n")
                    time.sleep(2)
                    print("You Win {} chips!\n".format(player.bet * 3 / 2))
                    time.sleep(3)
                    player.bankroll += player.bet * 3 / 2
                    break
                elif player.hand_check() == "Valid":
                    hand_valid = True

            #2)Stand

            if bj_menu == 2:

                #Phase 2.4 - Dealer Actions

                print("The Dealer flips his second card...\n")
                time.sleep(4)
                print("The Dealer reveals the {}\n".format(dealer.hand[1]))
                time.sleep(2)
                print(dealer.dealer_show_hand())
                time.sleep(4)
                print("---")
                while dealer.hand_value() < 17:
                    print("The Dealer hits...\n")
                    time.sleep(2)
                    dealer.draw(deck)
                    print("...the {}".format(dealer.hand[-1]))
                    print("---\n")
                print("The Dealer has {}\n".format(dealer.hand_value()))
                time.sleep(2)

                # Phase 2.5 - Deciding a Winner and Payouts

                if dealer.hand_value() > 21:
                    print("The Dealer Busts!\n")
                    time.sleep(2)
                    print("You Win {} chips!\n".format(player.bet))
                    time.sleep(2)
                    player.bankroll += player.bet
                    break
                if player.hand_value() > dealer.hand_value():
                    print("You have {}\n".format(player.hand_value()))
                    time.sleep(2)
                    print("You Win {} chips!\n".format(player.bet))
                    time.sleep(2)
                    player.bankroll += player.bet
                    break
                elif player.hand_value() < dealer.hand_value():
                    print("You have {}\n".format(player.hand_value()))
                    time.sleep(2)
                    print("You Lose {} chips!\n".format(player.bet))
                    time.sleep(2)
                    player.bankroll -= player.bet
                    break
                else:
                    print("You have {}\n".format(player.hand_value()))
                    time.sleep(2)
                    print("You and The Dealer Pushed!\n")
                    time.sleep(1)
                    break

            #3)Double Down

            elif bj_menu == 3:
                if len(player.hand) > 2:
                    print("You cannot double down after hitting!\n")
                elif player.bankroll < player.bet *2:
                    print("You do not have enough money to double down!\n")
                else:
                    print("You double your bet from {} to {}.".format(player.bet, player.bet * 2))
                    time.sleep(3)
                    player.bet = player.bet * 2
                    player.draw(deck)
                    print(player.show_hand())
                    print(time.sleep(3))
                    print("---")
                    if player.hand_check() == "Bust":
                        break
                    elif player.hand_check() == "Blackjack":
                        break
                    elif player.hand_check() == "Valid":
                        hand_valid = True

                    # Phase 3.4 - Dealer Actions

                    print("The Dealer flips his second card...\n")
                    time.sleep(4)
                    print("The Dealer reveals the {}\n".format(dealer.hand[1]))
                    time.sleep(2)
                    print(dealer.dealer_show_hand())
                    time.sleep(4)
                    print("---")
                    while dealer.hand_value() < 17:
                        print("The Dealer hits...\n")
                        time.sleep(2)
                        dealer.draw(deck)
                        print("...the {}".format(dealer.hand[-1]))
                        print("---\n")
                    print("The Dealer has {}\n".format(dealer.hand_value()))
                    time.sleep(2)

                    # Phase 3.5 - Deciding a Winner and Payouts

                    if dealer.hand_value() > 21:
                        print("The Dealer Busts!\n")
                        time.sleep(2)
                        print("You Win {} chips!\n".format(player.bet))
                        time.sleep(2)
                        player.bankroll += player.bet
                        break
                    if player.hand_value() > dealer.hand_value():
                        print("You have {}\n".format(player.hand_value()))
                        time.sleep(2)
                        print("You Win {} chips!\n".format(player.bet))
                        time.sleep(2)
                        player.bankroll += player.bet
                        break
                    elif player.hand_value() < dealer.hand_value():
                        print("You have {}\n".format(player.hand_value()))
                        time.sleep(2)
                        print("You Lose {} chips!\n".format(player.bet))
                        time.sleep(2)
                        player.bankroll -= player.bet
                        break
                    else:
                        print("You have {}\n".format(player.hand_value()))
                        time.sleep(2)
                        print("You and The Dealer Pushed!\n")
                        time.sleep(1)
                        break

    elif start_game == 5:
        #player.play = False
        sys.exit()
