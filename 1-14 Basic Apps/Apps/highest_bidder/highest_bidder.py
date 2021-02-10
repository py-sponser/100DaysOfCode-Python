import os
from arts import logo


def add_bidders(name,value):
    """Adding bidders (their name, their value) to a dictionary"""
    bidders[name] = value

def check_highest_bidder(bidders):
    """Checking who's the highest bidder"""
    highest_bidder = "" # defining an empty string (highest_bidder)
    values = list() # defining a list
    for bidder, value in bidders.items(): # iterating through keys and values of bidders dictionary (bidders, bids)
        values.append(value) # appending bids to the list
    highest_value = max(values) # getting the maximum number exist in the list
    for bidder in bidders: # iterating through keys
        if bidders[bidder] == highest_value: # checking which key (bidder) has that detected highest_value
            highest_bidder = bidder # saving the name of highest_bidder 
    print(f"[+] The winner is '{highest_bidder}' with bid of ${highest_value}!") # displaying the highest bidders and his bid


if __name__ == "__main__":
    print(f"{logo}\n")
    bidders = dict() # defining a dictionary
    name = str(input("[+] Enter name > ")) # asking for name
    value = int(input("[+] Enter bid > $")) # asking for bid
    while True:
        add_bidders(name,value) # calling add_bidders function to add the given bidders
        
        choice = input("[+] Any other bidders? type 'yes' or 'no'.\n") # asking whether there're other bidders or not
        os.system("clear") # clearing console, ui purpose
        if choice == "yes": # if user's choice is yes
            name = str(input("[+] Enter name >  ")) # asking for name
            value = int(input("[+] Enter bid > $")) # asking for bid
            add_bidders(name,value) # calling add_bidders function to add the given bidders
        elif choice == "no": # if no
            check_highest_bidder(bidders) # calling check_highest_bidder function with passing the bidders dictionary
            break # closing the app
        else: # if unexpected input from user
            print("[-] Wrong Entry!\n============================================") # display this message, then loop will continue
    
