# a word guessing game
# user should guess letters of unknown random word, every wrong guess, a life is lost

import random, os
from arts import stages, logo
from wordlist import wordlist

def reset_user_word(user_word,word_length):
    """Resting user word"""
    user_word.clear() # clearing the list of user_word
    for i in range(word_length): # loop that repeats by the number of word_length
        user_word.append("_") # appending underscores in user_word to be displayed as _ _ _ _ _ _ ...
    return user_word # return user_word list

def refresh(word,word_length):
    """refreshing (randomizing) the word to be guessed and its length"""
    word = random.choice(wordlist) # choosing random choice from wordlist list
    word_length = len(word) # getting the length of the word
    return word, word_length # returning both

def reset_lives(lives):
    """Resetting lives that got expired"""
    lives = len(stages) # setting lives to length of stages list which are drawings that displays each time a user guess wrong letter
    return lives # returning lives


def play(word,word_length,user_word,lives):
    """Starts the game"""
    while True:   # infinit loop
        print(" ".join(user_word),"\n") # printing user_word which will be a number of underscores separated by space (because of join function and space in " ") > _ _ _ _ ..
        guess = input("Guess a letter > ").lower() # asking a letter from user and lowering it
        os.system("clear") # clearing console for ui purpose
        if guess in user_word: # checking whether the success guess that the user guessed is already replaced with _ and exist in his word or not 
            print(f"{guess} is already exist!") # if exist, displaying that the letter exists
            
        for i in range(word_length): # iterating the number of word to be guessed length times
            if word[i] == guess: # if a word of index i is equal to the user's guess
                user_word[i] = guess # replacing the underscore of index i in user's word (which in same place as it exists in the word) by the user's guess(related to same place of letter in the word)
                
                #guessed_trueletters[word.index(guess)]=guess >>>>>>>>>>>> # works if no repeated characters 
        
        
        
        if guess not in word: # if user's guess is not in the word
            lives -= 1 # 1 life lost
            print(stages[lives]) # display the first draw warning from stages list 
            if lives == 0: # if lives is 0 (after many lives lost)
                print("You lost! :(\n===============================================================================") # user loses
                word,word_length = refresh(word,word_length) # refreshing the word and its length
                user_word = reset_user_word(user_word,word_length) # resetting user_word depending on word_length that got refreshed
                lives = reset_lives(lives) # resetting lives
                break # close the current loop, so that the user will be asked whether he wants to play or not as if game hasn't closed yet

        if "_" not in user_word: # if _ is not in user_word (which means that user has completed the word and won before lives expire)
            print(" ".join(user_word)) # display the word complated
            print("You Won! :)\n===============================================================================") # user won
            word,word_length = refresh(word,word_length) # refreshing them
            user_word = reset_user_word(user_word,word_length) # resetting them
            lives = reset_lives(lives) # resetting lives
            break # close the current loop, so that the user will be asked whether he wants to play or not as if game hasn't closed yet

word = "" # defining string for a word to guess
word_length = int() # defining an int for word length
word, word_length = refresh(word,word_length) # calling refresh function which its name means something that'll be understood
# and it's also responsible for giving random values for the word and word length

user_word = list() # defining a list for user's word
user_word = reset_user_word(user_word,word_length) # reseting user word (calling the function), will be explained

lives = int() # defining an integar for number of lives which when expire by guessing the wrong letters of the word n times, user loses
lives = reset_lives(lives) # resetting lives by calling its function
print(logo,'\n\n') # displaying logo

while True:
    choice = input("[+] play? (y/n)>  ") # asking user whether he wants to play or not
    if choice == "y" or choice == "yes" or choice == "play": # if user's choice is yes
        play(word,word_length,user_word,lives) # call play function with passing the word, word_length, user_word, lives
    elif choice == "n" or choice == "no" or choice == "exit" or choice == "quit": # if no
        break # close the game
    else: # if unexpected input
        print("[-] Wrong Entry!, please choose y/n (yes/no)!") # display this message, then loop reloads