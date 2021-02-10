# number guessing game, there're 2 modes:
# easy mode : user has 10 attempts to guess the right number, whenever he guess a wrong number
# a hint is provided which is whether the last wrong guess is lower than the right number or greater till user guess it right
# hard more: the difference is that there's only 5 attempts


import random, os
from arts import logo

def easy_game(number): 
    """easy game mode, enables 10 attempts to guess the right random number"""
    attempts = 10 # number of attempts of easy game mode
    while True: # infinite loop
        print(f"You have {attempts} remaining to guess the number.")  # displaying how many attempts left for the player
        if attempts == 0: # if no attempts left
            print("Attempts expired, You lose!") # message to the user
            break # exit the loop
        user_guess = int(input("Guess a number> ")) # in case attempts left, take a guess from the player
        if user_guess > number: # if player's guess is greater than the random number
            os.system("clear") # clearing the console, for ui purpose
            print("Too high.\nGuess again.") # letting player know that the guess is greater than the random number.
            attempts -= 1 # decreasing attempts by 1
        elif user_guess < number: # if player's guess is lower than the random number.
            os.system("clear") # clearing the console, for ui purpose
            print("Too low.\nGuess again.") # letting player know that the guess is lower than the random number.
            attempts -= 1 # decreasing attempts by 1
            
        elif user_guess == number: # if player guessed the right random number
            print(f"You get it, It's {user_guess}\nYou win!") # he wins
            break # exit the loop

def hard_game(number):
    """hard game mode, enables 5 attempts to guess the right random number"""
    attempts = 5 # number of attempts of hard game mode
    while True: # infinit loop
        print(f"You have {attempts} remaining to guess the number.") # displaying how many attempts left for the player
        if attempts == 0: # if no attempts left
            print("Attempts expired, You lose!") # player lose
            break # exit the loop
        user_guess = int(input("Guess a number> ")) # if attempts left, take a guess from the player
        if user_guess > number: # if player's guess is greater than the random number
            os.system("clear") # clearing the console, for ui purpose
            print("Too high.\nGuess again.") # letting player know that the guess is greater than the random number.
            attempts -= 1 # decreasing attempts by 1 
        elif user_guess < number: # if player's guess is lower than the random number
            os.system("clear") # clearing the console, for ui purpose
            print("Too low.\nGuess again.")  # letting player know that the guess is lower than the random number.
            attempts -= 1 # decreasing attempts by 1
            
        elif user_guess == number: # if player guessed the right random number
            print(f"You get it, It's {user_guess}\nYou win!") # he wins
            break # exit the loop
        

if __name__ == "__main__": # execute any rest of code starting after this check
    print(f"{logo}\n")
    print("Welcome to the number guessing game.") # welcome to game
    print("Think of a number between 1 and 100.") # game idea
    number = random.randint(1,100) # getting a random number that a player should guess

    while True: # infinit loop
        level_choice = str(input("Choose a difficulty level, Type 'easy' or 'hard'> ")) # player should choose whether he wants the game easy or hard
        os.system("clear") # clearing the console, for ui purpose
        if level_choice == "easy": # if player's choice is easy
            easy_game(number) # call the easy_game function above with passing the random number to it
            break # exit the loop (exit the game)
        elif level_choice == "hard": # if player's choice is hard
            hard_game(number) # call the hard_game function above with passing the random number to it
            break # exit the loop (exit the game)
        else: # if player's choice is not easy or hard
            print("Wrong Entry!\=================================================") # display a 'Wrong Entry!' message to him
            continue # reload the loop
