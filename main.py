############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################

import random
from replit import clear
from art import logo
play_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game():
    play_game = True
    print (logo)
    player_hand = random.sample(cards, 2)
    player_score = sum(player_hand)
    computer_hand = random.sample(cards, 2)
    computer_score = sum(computer_hand)
        
    print(f"    Your card: {player_hand}, current score: {player_score}")
    print(f"    Computer's first card: {computer_hand[0]}")
    
    while play_game:
        if player_score <21:
            if input("\nType 'y' to get another card, type 'n' to pass: ") == "y":
                player_hand.append(random.choice(cards))
                player_score = sum(player_hand)
                if player_hand[-1] == 11:
                    if player_score > 21:
                        player_hand[-1] = 1
                        player_score = sum(player_hand)
                print(f"\n    Your card: {player_hand}, current score: {player_score}")
                print(f"    Computer's first card: {computer_hand[0]}")
            else:
                play_game = False
        else:
            play_game = False
    
    while computer_score <17:
        computer_hand.append(random.choice(cards))
        computer_score = sum(computer_hand)
    
    print(f"\n    Your final hand: {player_hand}, final score: {player_score}")
    print(f"    Computer's first hand: {computer_hand}, final score: {computer_score}")
    if player_score > 21 and computer_score >21:
        print ("You lose 😩\n")
    elif player_score > 21:
        print ("You went over. You lose 😩\n")
    elif computer_score == 21:
        print("Lose, opponent have Blackjack 😱\n")
    elif player_score == 21:
        print("You have Blackjack. You win! 😁\n")
    elif player_score > 21:
        print ("Opponent went over. You win 😁\n")
    elif player_score > computer_score:
        print ("You won 😉\n")
    elif player_score == computer_score:
        print ("It's draw 🤪 \n")


while play_game:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        clear()
        game()
    else:
        play_game = False

