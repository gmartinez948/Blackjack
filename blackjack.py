"""
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

"""
import random 

ans = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = {}
current_score = {}
dealers_cards = {}
''' 
this first function uses the first prompt to route the user's decision.
Once that is determined, and if yes, the function will randomize a random number
from the cards list and then append those values to a dictionary to compare hands
between the player and dealer
'''
def play_game(ans, cards):
    if ans == 'y':
        for card in range(len(cards)):
            player_card1 = random.choice(cards)
            player_card2 = random.choice(cards)
            player_cards['Your Cards'] = [player_card1, player_card2]
                    # trying to add up the sum of the values of ['Your Cards']
            current_score["Your score"] = [player_card1 + player_card2]
            dealers_cards["Dealer's hand"] = [random.choice(cards)]
        print(f"{player_cards}, {current_score}, \n{dealers_cards}")
        if current_score["Your score"] == 21:
            print('You win!')
    elif ans == 'n':
        print("Goodbye")
        exit()
    else:
        print("You did not enter 'Y or 'N', please try again")
        exit()

play_game(ans, cards)

ans2 = input("Type 'y' to pull another card, Type 'n' to pass: ")

dealers_cards["Dealer's hand"].append(random.choice(cards))
final_player_score = {}
dealer_final_score = {}

''' Creating a function that if the player wants to pull another card, 
the function will tally the current score, show cards in cards list, 
and determine a winner. if no card is pulled, 
the dealer's hand is revealed and a winner is determined.
'''
def continue_playing(ans2, play_game):
    if ans2 == 'y':
        for card in range(len(cards)):
            dealer_random_card = random.choice(cards)
            random_playercard3 = random.choice(cards)
        '''
        Ace can either be 2 or 11. If random # from cards list is 2 and 
        current score is less than or equal to 10 this will add 10. 
        The following code does the reverse
        '''
        if random_playercard3 == 2 and current_score['Your score'] <= 12:
            random_playercard3 += 9
        elif random_playercard3 == 11 and current_score['Your score']>= 12:
            random_playercard3 -= 9
        player_cards['Your Cards'].append(random_playercard3)
        current_score["Your score"].append(random_playercard3)
        final_player_score['Your final score'] = sum(current_score['Your score'])
        dealer_final_score["Dealer's hand"] = sum(dealers_cards["Dealer's hand"])
        print(f"{player_cards}, {final_player_score}, \n{dealer_final_score}")
        '''
        Going through all possible results, and determining a win, tie,or loss by comparing booleans
        '''
        if final_player_score['Your final score'] == 21: 
            print("You win!")
        elif final_player_score['Your final score'] > 21:
            print('You Lose!')
        elif final_player_score['Your final score'] == dealer_final_score["Dealer's hand"]:
            print("it's a tie!")
        elif dealer_final_score["Dealer's hand"] > 21 and final_player_score['Your final score'] < 21:
            print("You Win!")
        elif final_player_score['Your final score'] < dealer_final_score["Dealer's hand"] and dealer_final_score["Dealer's hand"] <= 21:
            print("You Lose!")
        elif final_player_score['Your final score'] > dealer_final_score["Dealer's hand"] and final_player_score['Your final score'] < 21:
            print('You win!')
    elif ans2 == 'n':
        final_player_score['Your final score'] = sum(current_score['Your score'])
        dealer_final_score["Dealer's hand"] = sum(dealers_cards["Dealer's hand"])
        print(f"{player_cards}, {final_player_score}, \n{dealer_final_score}")
        if final_player_score['Your final score'] > 21:
            print('You Lose!')
        elif final_player_score['Your final score'] == dealer_final_score["Dealer's hand"]:
            print("it's a tie!")
        elif dealer_final_score["Dealer's hand"] > 21 and final_player_score['Your final score'] < 21:
            print("You Win!")
        elif final_player_score['Your final score'] < dealer_final_score["Dealer's hand"] and dealer_final_score["Dealer's hand"] <= 21:
            print("You Lose!")
        elif final_player_score['Your final score'] > dealer_final_score["Dealer's hand"] and final_player_score['Your final score'] < 21:
            print('You win!')
    else:
        print("You did not enter 'y' or 'n', please start over")
        exit()
            
continue_playing(ans2, play_game)

'''
Improvements that can be made:
- prompt the user to play again.
- any way to make code shorter?
- if user enter's wrong input (not y or n), 
    prompt the user to try the previous execution again
'''
            
        
       