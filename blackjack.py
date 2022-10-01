import art
import random
import os



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = cards[random.randint(0,(len(cards)-1))]
    return card

def calculate_value(cards_amount):

    total = sum(cards_amount)

    for card in cards_amount:
        if total > 21:
            if card == 11:
                cards_amount.remove(card)
                cards_amount.append(1)
                total = sum(cards_amount)

    if sum(cards_amount) == 21:
        total = 0

    return total

def compare(player, dealer):
    if player > dealer and player < 21:
        return print(f"You've lost\nPlayer Score : \n{player}\nDealer Score:\n{dealer}")
    elif player < dealer and dealer < 21:
        return print(f"You've lost\nPlayer Score : \n{player}\nDealer Score:\n{dealer}")
    elif player == dealer:
        return print(f"Draw\nPlayer Score : \n{player}\nDealer Score:\n{dealer}")

def blackjack():
    print (art.logo)
    print("Welcome to Blackjack")
    player_cards = []
    dealer_cards = []

    # BlackjackStart #

    # Player first card deal
    player_cards.append(deal_card())
    player_cards.append(deal_card())
    player_score = calculate_value(player_cards)

    # Dealer first card deal
    dealer_cards.append(deal_card())
    dealer_cards.append(deal_card())
    dealer_score = calculate_value(dealer_cards)


    print(player_cards)
    print(player_score)

    # Player if sum of cards < 21 and not = blackjack
    if player_score < 21 and player_score > 0:
        still_draws = True

    elif player_score == 0:
        print("You've won!")
        still_draws = False

    else:
        still_draws = False

    while still_draws:

        deal_again = input("do you want to draw a card again? (Y/N) : ").lower()

        if deal_again == "y":

            player_cards.append(deal_card())
            player_score = calculate_value(player_cards)
            print(player_cards)
            print(player_score)

            if player_score > 21:
                still_draws = False
                print("You've gone over 21, dealer won!")

            elif player_score == 0 :
                print("You've won! Blackjack")


        else:
            still_draws = False

            if dealer_score == 0:
                print("You've Lost, the Dealer got Blackjack")

    # Blackjack Dealer Start :

    dealer_draws = False
    dealer_score = calculate_value(dealer_cards)

    if dealer_score > 0 and dealer_score < 17:
        dealer_draws = True

    while dealer_draws :
        dealer_cards.append(deal_card())
        dealer_score = calculate_value(dealer_cards)
        if dealer_score > 17 or dealer_score == 0:
            dealer_draws = False

    print(compare(calculate_value(player_cards), calculate_value(dealer_cards)))

    play_again = input(("Do you want to play again (y/n): "))
    if play_again == "y":
        blackjack()

blackjack()