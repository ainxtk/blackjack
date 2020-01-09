"""
Title: Blackjack game
Author: Micky Kumar
Verison: 1.0
Created: December 2019


"""



from random import randint


### The get_card() and get_hand_total() can easily be changed if I decide that
### I would like to add face cards into the game. Actually, I would not even need
### to change any of the code in the main play_game() function to implement this!

### Keeping the design of your program
### to be modular is extremely important! A little planning at the beginning can save
### a lot of time if something needs to be changed in the future.
def get_card():
    """
    Creaate a random number  between 1 to 10
    """
    return randint(1,10)

def get_hand_total(hand):
    """
    Sum hand
    """
    return sum(hand)

def play_game():
    """
    main code
    """
    player_hand=[get_card(), get_card()]
    dealer_hand=[get_card(), get_card()]
    print ("-----------------------------------------------------------------------")
    print("|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |")
    print("| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |")
    print("| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |")
    print("| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|")
    print("`------'`------'`------'`------'`------'`------'`------'`------'`------'")
    print(".------..------..------..------.")
    print("|G.--. ||A.--. ||M.--. ||E.--. |")
    print("| :/\: || (\/) || (\/) || (\/) |")
    print("| :\/: || :\/: || :\/: || :\/: |")
    print("| '--'G|| '--'A|| '--'M|| '--'E|")
    print("`------'`------'`------'`------'")

    print ("--------------------------------------------")
    print(f'Your hand is {player_hand} - {get_hand_total(player_hand)}')
    print(f'Dealer has start with [{player_hand[0]}, X]')

    #player logic
    while(get_hand_total(player_hand) <= 21):
        while(True):
            player_option = input("[H]it or [S]tay? ").upper()
            if(player_option in ["H", "S"]):
                break

        if(player_option=="S"):
            break
        elif(player_option == "H"):
            player_hand.append(get_card())
            print(f'Your hand is now: {player_hand} - {get_hand_total(player_hand)}')

    if(get_hand_total(player_hand)>21):
        print("Bust! You have lost! :(")
        print(f'Dealer hand was: {dealer_hand} - {get_hand_total(dealer_hand)}')
        return

    #dealer logic
    while(get_hand_total(dealer_hand) < 17):
        dealer_hand.append(get_card())

    print(f'Dealer hand is now: {dealer_hand} - {get_hand_total(dealer_hand)}')

    if(get_hand_total(player_hand)>21):
        print("Dealer Bust! You have won! :)")
        return

    #check winner if no one busted
    if(get_hand_total(player_hand)>get_hand_total(dealer_hand)):
        print("You have won! :)")
    else:
        print("You have lost! :(")


if __name__ == '__main__':
    user_ans = 'Y'
    while(True):
        if(user_ans=='Y'):
            play_game()
        elif(user_ans=='N'):
            break

        user_ans = input('Would you like to play again? (Y/N): ').upper()
