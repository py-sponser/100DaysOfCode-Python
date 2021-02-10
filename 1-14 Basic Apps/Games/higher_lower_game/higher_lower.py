"""
1- Generate random number to display random game data for comparisons.
2- Display the data for comparison.
3- Order user to guess who has higher followers!
4- check user's input, if A is higher or B, according to number of followers.
"""
from game_data import data
from arts import logo, vs
import random, os


def check_followers(random_data1,random_data2, user_choice):
    """check user's input, if A is higher or B, according to number of followers"""

    if user_choice == "A".lower(): # if user's input is a
        if random_data1["follower_count"] > random_data2["follower_count"]: # if followers of a is higher than b
            return "a" # return a

        else: # if not
            return False # return false (or any other value other than a or b)

    if user_choice == "B".lower(): # if user's input is b
        if random_data1["follower_count"] < random_data2["follower_count"]: # if followers of b is higher than a
            return "b" # return b
            
        else: # if  not
            return False # return false (or any other value other than a or b)



if __name__ == "__main__":
    print(f"{logo}\n") # printing logo
    score = 0 # initializing score with 0
    last_a = None # last info that user picked will be saved in it, to show it as first info 'A' to compare with second random info 'B'
    a_right = None # a boolean set to None 
    random_data1 = data[random.randint(0,len(data)-1)] # getting the first data from the list of dictionaries 'data' depending on random index between 0 and length of 'data' list
    random_data2 = data[random.randint(0,len(data)-1)] # getting the second data in same way.
    win = None # a boolean set to None

    while True: # infinit loop

        if a_right: # if data of 'a' is right
            random_data1 = last_a # let the random_data1 that represents 'a' equal to the correct last_a that user chose!
            random_data2 = data[random.randint(0,len(data)-1)] # get a random data for 'b'

        elif a_right != None and a_right == False: # if 'a' is False and not None
            random_data1 = data[random.randint(0,len(data)-1)] # get a new random data for 'a'
            random_data2 = last_a # let 'b' equal to the correct last_a that user chose!

        a_right = None # setting a_right to None for next loops

        if random_data1["name"] == random_data2["name"] or random_data1["follower_count"] == random_data2["follower_count"]: # checking if in both data, names are identical or number of follower are identical, if yes, loop will continue
            continue

        print(f"Compare!\n\n") # printing a text
        if random_data2 != last_a: # if 'b' is not last_a, means that 'b' hadn't the highest number of followers
            if win: # if first win occurred
                print(f"[+] You are right, your current score = {score}.") # print this statement that contains the score, and will be printed till game ends
            print(f"A: {random_data1['name']}, a {random_data1['description']}, from {random_data1['country']}.\n{vs}\n\n") # display default data, whether 'a' is last_a or new random 'a'.
            print(f"B: {random_data2['name']}, a {random_data2['description']}, from {random_data2['country']}.\n\n") # display default data for 'b'
        elif random_data2 == last_a: # if 'b' is last_a, means that 'b' had the highest number of followers
            if win: # if first win occurred
                print(f"[+] You are right, your current score = {score}.") # print this statement that contains the score, and will be printed till game ends
            print(f"A: {random_data2['name']}, a {random_data2['description']}, from {random_data2['country']}.\n{vs}\n\n") # display 'b' as last_a in place of 'a'
            print(f"B: {random_data1['name']}, a {random_data1['description']}, from {random_data1['country']}.\n\n") # display 'a' in place of 'b'

        # if you want to show the number of followers of 'a' (or last_a), you can just add {random_data1['follower_count']} to the print statement of "A" exactly above.


        user_choice = input("- Who has higher number of followers? Type 'A' or 'B'\n> ") # getting input from user
        os.system("clear") # clearing terminal/cmd content (ui purpose)
        if user_choice == "A".lower() or user_choice == "B".lower(): # if user's input is a or b, dive in the logic
            check_result = check_followers(random_data1=random_data1,random_data2=random_data2, user_choice=user_choice) # check the result of followers checkings in the function above
            if check_result == "a": # if 'a' == 'a'
                win = True # set win to true (will be always true after first win, to show the statement of score till loss)
                score += 1 # score get inceremented by 1
                a_right = True # first data 'a' set to True
                last_a = random_data1 # saving value of random_data1 'a' in last_a

            elif check_result == "b": # if 'b' == 'b'
                win = True # set win to true (will be always true after first win, to show the statement of score till loss)
                score += 1 # score get inceremented by 1
                a_right = False # first data 'a' set to True
                last_a = random_data2 # saving value of random_data2 'b' in last_a
            else: # if result of checking neither 'a' nor 'b' 
                print(f"[+] Oh, That's wrong, your final score is: {score}.") # displaying last message of loss and final score
                break # closing the loop (closing the game)
        else: # if user hasn't entered either 'a' or 'b'
            print("Wrong Entry!") # display this message, the loop continues

