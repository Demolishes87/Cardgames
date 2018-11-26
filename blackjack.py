from classes import *
import time
import sys

#Pre Game Control Flow
#Pre Game Phase 1 - Welcome user, get player name.
print("Hello! Welcome to Blackjack!\n")
#time.sleep(2)
player = Player(str(input("What is your name?: ")))
print("---")
print("Hi {}, Good Luck!\n---".format(player.name))
#time.sleep(2)

#Pre Game Phase 2 - Create 8 Decks and the Dealer

deck = Deck(8)
dealer = Dealer("Dickhead")

#Pre Game Phase 3 - Shuffle the 8 Decks and insert the cut card

deck.shuffle()

#deck.insert_cut_card() IMPLEMENT NEXT

#Pre Game Phase 4 - Set initial bankroll

player.chips()


#Game Flow

#Phase One - Instantiate game menu


while player.play:

    start_game = player.play_menu()

    hand_valid = True

    if start_game == 1:
        player.turn = 0
        player.insurance = 0
        dealer.hand = []
        player.hand = []
        if player.bankroll == 0:
            print("You are all out of chips!")
            time.sleep(2)
            player.buy_more_chips()

        #Phase Two - Take Player Bet and Deal Cards
        player.take_bet()
        print("---")
        print("...Dealing Cards...")
        #time.sleep(1.5)
        print("---")
        #player.draw(deck)
        #dealer.draw(deck)
        #player.draw(deck)
        #dealer.draw(deck)

        #USE TO TEST HANDS
        player.hand = [Card("Hearts", "Ace"), Card("Hearts", "King")]
        dealer.hand = [Card("Hearts", "Ace"), Card("Hearts", "5")]

        #Phase Three - Displaying Dealer and Player Hands

        print(dealer.show_upcard())
        #time.sleep(1.5)
        print("\nYou have the {} and the {}".format(player.hand[0], player.hand[1]))
        #time.sleep(2)
        print("---")

        while hand_valid:

            #Phase 4 - Check for insurance and Initial Blackjacks
            #Insurance
            if dealer.insurance_flag == True and player.turn == 0:
                player.insurance = player.bet / 2
                if player.hand_value() == 21:
                    decision = input("Do you want even money payout (Y/N)?: ")
                    if decision == "Y":
                        print("You take even money on your bet, and win {}!".format(player.bet))
                        time.sleep(3)
                        print("---")
                        player.bankroll += player.bet
                        break
                    if decision == "N":
                        insurance_decision = input("Would you like to take insurance (Y/N)?: ")
                        if insurance_decision == "Y":
                            print("\nYou pay {} for insurance".format(player.insurance))
                            print("---")
                            # time.sleep(2)
                            print("The Dealer checks for Blackjack...\n")
                            # time.sleep(3)
                            if dealer.dealer_hand_check() == "Blackjack":
                                print("...The Dealer reveals the {}".format(dealer.hand[1]))
                                print("---")
                                # time.sleep(2)
                                print("The Dealer has Blackjack!\n")
                                # time.sleep(2)
                                print("You won {} from your insurance bet...\n".format(player.insurance))
                                time.sleep(2)
                                print("...But you pushed on your hand!".format(player.bet))
                                time.sleep(2)
                                print("---")
                                player.bankroll += player.bet
                                # time.sleep(2)
                                dealer.insurance_flag = False
                                hand_valid = False
                                break
                            else:
                                print("...The Dealer does not have Blackjack")
                                print("---")
                                # time.sleep(2)
                                print("You lose your insurance bet of {}...\n".format(player.insurance))
                                time.sleep(2)
                                print("...But you win your bet of {}".format(player.bet))
                                time.sleep(2)
                                print("---")
                                # time.sleep(3)
                                player.bankroll += player.bet
                                dealer.insurance_flag = False
                                hand_valid = False
                                break

                if player.insurance + player.bet < player.bankroll:
                    insurance_decision = input("Would you like to take insurance (Y/N)?: ")
                    if insurance_decision == "Y":
                        print("\nYou pay {} for insurance".format(player.insurance))
                        print("---")
                        #time.sleep(2)
                        print("The Dealer checks for Blackjack...\n")
                        #time.sleep(3)
                        if dealer.dealer_hand_check() == "Blackjack":
                            print("...The Dealer reveals the {}".format(dealer.hand[1]))
                            print("---")
                            #time.sleep(2)
                            print("The Dealer has Blackjack!\n")
                            #time.sleep(2)
                            print("You pushed because you took insurance!".format(player.bet))
                            print("---")
                            #time.sleep(2)
                            dealer.insurance_flag = False
                            hand_valid = False
                            break
                        else:
                            print("...The Dealer does not have Blackjack")
                            print("---")
                            #time.sleep(2)
                            print("You lose your insurance bet of {}".format(player.insurance))
                            print("---")
                            #time.sleep(3)
                            player.bankroll -= player.insurance
                            dealer.insurance_flag = False
                    elif insurance_decision == "N":
                        if dealer.dealer_hand_check() == "Blackjack":
                            print("...The Dealer reveals the {}\n".format(dealer.hand[1]))
                            #time.sleep(2)
                            print("The Dealer has Blackjack!\n")
                            time.sleep(2)
                            print("You lose {} chips!".format(player.bet))
                            player.bankroll -= player.bet
                            player.bet = 0
                            print("---")
                            dealer.insurance_flag = False
                            hand_valid = False
                            break
                        else:
                            print("\nThe Dealer checks for Blackjack...")
                            #time.sleep(3)
                            print("...The Dealer does not have Blackjack")
                            print("---")
                            #time.sleep(2)
                            dealer.insurance_flag = False
            #Blackjacks
            if dealer.dealer_hand_check() == "Blackjack" and player.turn == 0:
                print("...The Dealer reveals the {}\n".format(dealer.hand[1]))
                #time.sleep(2)
                print("The Dealer has Blackjack!\n")
                if player.hand_value() == 21:
                    print("But you also have Blackjack!\n")
                    #time.sleep(1)
                    print("You and the Dealer pushed!\n")
                    #time.sleep(2)
                    hand_valid = False
                    break
                elif player.hand_value() != 21:
                    print("You lost {}!".format(player.bet))
                    print("---")
                    player.bankroll -= player.bet
                    #time.sleep(2)
                    hand_valid = False
                    break
            elif player.hand_value() == 21 and player.turn == 0:
                print("You Have Blackjack!\n")
                #time.sleep(2)
                print("You win {} chips!\n".format(player.bet * 3/2))
                #time.sleep(3)
                player.bankroll += player.bet * 3/2
                break

            #Phase Five - Player Actions

            bj_menu = player.bj_menu()

            #1)Hit

            dealer.insurance_flag = False
            if bj_menu == 1:
                player.turn += 1
                player.draw(deck)
                print("You hit the {}\n".format(player.hand[-1]))
                #time.sleep(2)
                print(player.show_hand())
                #time.sleep(2)
                print(dealer.show_upcard())
                #time.sleep(2)
                print("---")
                if player.hand_check() == "Bust":
                    hand_valid = False
                    #break
                elif player.hand_check() == "Blackjack":
                    hand_valid = False
                    #break
                elif player.hand_check() == "Valid":
                    hand_valid = True

            #2)Stand
            if bj_menu == 2:
                player.turn += 1
                print("\nYou stand on {}.\n".format(player.hand_value()))
                print("---")
                #time.sleep(2)

                #Phase Six.2 - Dealer Actions

                print("The Dealer flips his second card...\n")
                #time.sleep(4)
                print("The Dealer reveals the {}\n".format(dealer.hand[1]))
                #time.sleep(2)
                print(dealer.dealer_show_hand())
                #time.sleep(4)
                print("---")
                while dealer.hand_value() < 17:
                    print("The Dealer hits...\n")
                    #time.sleep(2)
                    dealer.draw(deck)
                    print("...the {}".format(dealer.hand[-1]))
                    print("---\n")
                    #time.sleep(2)
                print("The Dealer has {}\n".format(dealer.hand_value()))
                #time.sleep(2)

                # Phase Seven.2 - Deciding a winner and Payouts

                if show_down(dealer.hand_value(), player.hand_value(), player.bet, player.bankroll) == "win":
                    player.bankroll = player.bankroll + player.bet
                else:
                    player.bankroll = player.bankroll - player.bet
                break

            #3)Double Down

            elif bj_menu == 3:
                player.turn += 1
                if len(player.hand) > 2:
                    print("You cannot double down after hitting!\n")
                elif player.bankroll < player.bet *2:
                    print("You do not have enough money to double down!\n")
                else:
                    print("You double your bet from {} to {}.\n".format(player.bet, player.bet * 2))
                    #time.sleep(3)
                    player.bet = player.bet * 2
                    player.draw(deck)
                    print("You hit the {}\n".format(player.hand[-1]))
                    #time.sleep(2)
                    print(player.show_hand())
                    #time.sleep(2)
                    print(dealer.show_upcard())
                    #time.sleep(2)
                    print("---")
                    if player.hand_check() == "Bust":
                        hand_valid = False
                        #break
                    elif player.hand_check() == "Blackjack":
                        hand_valid = False
                        #break
                    elif player.hand_check() == "Valid":
                        hand_valid = True

                        # Phase Six.3 - Dealer Actions

                        print("The Dealer flips his second card...\n")
                        #time.sleep(4)
                        print("The Dealer reveals the {}\n".format(dealer.hand[1]))
                        #time.sleep(2)
                        print(dealer.dealer_show_hand())
                        #time.sleep(4)
                        print("---")
                        while dealer.hand_value() < 17:
                            print("The Dealer hits...\n")
                            #time.sleep(2)
                            dealer.draw(deck)
                            print("...the {}".format(dealer.hand[-1]))
                            print("---\n")
                            #time.sleep(2)
                        print("The Dealer has {}\n".format(dealer.hand_value()))
                        #time.sleep(2)

                        # Phase Seven.3 - Deciding a winner and Payouts

                        if show_down(dealer.hand_value(), player.hand_value(), player.bet, player.bankroll) == "win":
                            player.bankroll = player.bankroll + player.bet
                        else:
                            player.bankroll = player.bankroll - player.bet
                        break

    elif start_game == 5:
        sys.exit()
