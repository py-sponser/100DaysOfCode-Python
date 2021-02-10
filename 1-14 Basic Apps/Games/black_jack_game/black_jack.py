# black jack game.
# user take random numbers same as computer.
# the one who gets the highest values that its sum is <= 21, and his sum is greater than the other opponent, so he's the winner
# each opponent has the choice to append another word (card)
# the one who finds out that his list summition is greater than 21, is loser


import random, os
from arts import logo

def setting_cards(card):
    """Giving opponents inital random cards"""
    card.clear()
    for i in range(2):
        card.append(random.choice(numbers))

def winner(user_cards,computer_cards):
    final_message = f"[+] Your final hand> {user_cards}\n[+] Computer's final hand> {computer_cards}" # final message to show.
    if sum(computer_cards) > 17 and sum(computer_cards) <= 21: # computer must append values till sum is greater than 17 and <= highest_value (21)
        if sum(computer_cards) <= highest_value and sum(user_cards) <= highest_value: # computer and user sum must be <= highest_value
            # the lowest value result from (highest_value - computer's sum) or (highest_value and user's sum) is the winner
            if (highest_value - sum(user_cards)) < (highest_value - sum(computer_cards)): 
                # (highest_value and user's sum) < (highest_value - computer's sum)  
                # user wins
                print(final_message)
                print("You have greater cards than computer.")
                print("You Win!\n=============================================")
                user_win = True

                return user_win
            elif (highest_value - sum(user_cards)) > (highest_value - sum(computer_cards)):
                # (highest_value and user's sum) > (highest_value - computer's sum)
                # computer wins
                print(final_message)
                print("Computer has greater cards than you.")
                print("You lose\n==========================================")
                user_win = False
                return user_win
            elif (highest_value - sum(user_cards)) == (highest_value - sum(computer_cards)):
                # (highest_value and user's sum) = (highest_value - computer's sum)
                # no one wins, it's a draw!
                print(final_message)
                print("Draw!\n==============================================")
                user_win == "Draw"
                return user_win



def play(user_cards,computer_cards,user_win):
    
    while True:
        print(f"Your Current cards>{user_cards}\nComputer's first card> {computer_cards[0]}") # showing status for user
        computer_add_choice = random.choice(choices) # randomly answering for computer.
        random_value = random.choice(numbers) # having a random value for the next appendings

        user_add_choice = str(input("[+] Add another card? (y,n)\n> ")) # asking user to add more cards or not
        os.system("clear") # clearing console, ui purpose
        if user_add_choice == "y":  # if user accepts adding new cards
            user_cards.append(random_value) # add new card
            final_message = f"[+] Your final hand> {user_cards}\n[+] Computer's final hand> {computer_cards}" # final message
            if sum(user_cards) > highest_value: # if sum of user cards > highest_value, he loses
                print(final_message)
                print("You Lose!\n==============================================")
                break
            

        elif user_add_choice == "n": # if user denies adding new cards, and everytime he'll deny, because he actually monitor his list, knows that he can't add more or he loses, and wait for result against computer.
            if computer_add_choice == "y": # it's computer's turn, checking if yes.
                computer_cards.append(random_value) # add new card to computer's cards
                final_message = f"[+] Your final hand> {user_cards}\n[+] Computer's final hand> {computer_cards}" # same final message
                if sum(computer_cards) > highest_value: # if sum of computer's card < highest_value, computer loses
                    print(final_message)
                    print("Computer has cards greater than 21")
                    print("You Win\n==============================================")
                    break
                user_win = winner(user_cards,computer_cards) # final challenge btw user and computer, they passed checkings whether their sums are greater than highest_value or not
                if (user_win == False) or (user_win == True) or (user_win == "Draw"): 
                    break
                else:
                    continue
            elif computer_add_choice == "n": # if the computer's random choice is 'n', so it continues the loop, the user will deny accepting to add new cards.
                continue
        else: # validation purpose.
            print("Wrong Entry!\n==============================================")
            continue
        





highest_value = 21 # the value which whoever exceeds it, loses and whoever get the highest value approximately to it, wins
numbers = [11,2,3,4,5,6,7,8,9,10,10,10]

user_cards = list() # user cards
computer_cards = list() # computer cards
user_win = None
choices = ["y","n"] # choices to randomly choose for computer whether it adds values to its list or not.
print(f"{logo}\n")
while True:
    user_win = None
    
    setting_cards(user_cards) # giving user first 2 random values
    setting_cards(computer_cards) # giving computer first 2 random values
    choice = str(input("- Play blackjack? (y/n)\n> "))
    if choice == "y":
        play(user_cards,computer_cards,user_win)
    elif choice == "n":
        break
    else:
        print("[-] Wrong Entry!\n==================================================")
        continue
    

