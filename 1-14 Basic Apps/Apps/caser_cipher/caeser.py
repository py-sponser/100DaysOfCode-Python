from arts import logo
# this app encrypts words and numbers by implementing shifts on them (the famouse caeser cipher)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = [" ",'!', "@",'#', '$', '%', "^", '&', '(', ')', '*', '+',"-","_","+","/","|","?",">","<",";",":",",","'","."]

def get_user_input():
    """Getting data from user"""
    user_word = str(input("\n[+] Enter your message> "))  # asking user for the word
    while True: # infinit loop checking for shifts
        try: # trying getting the following
            shift = int(input("[+] Enter number of shifts> ")) # asking user for an integar number for shifts
        except: # if user entered unexpected value like a string intead of integar
            print("Please enter an integar number for shifts!\n") # display this message
            continue # reload the loop
        break # if user entered an integar number, close the loop
    return user_word, shift # return the word and shifts

def encode(user_word,shift):
    """Prints the word after it gets encrypted"""
    word = "" # creating a word variable
    for char in user_word: # iterating through every char in user_word
        if char in symbols:
            word += char
            continue
        elif char == "'":
            word += "'"
            continue
            

        elif char.isdigit(): # if a character is an integar number is found
            if user_word[user_word.index(char)-1] == "-":
                char = (int(char)*-1) + shift # converting character (number) from string to integar with incrementing it by a shift
            else: 
                char = int(char) + shift # converting character (number) from string to integar with incrementing it by a shift
                
            char = str(char) # converting character from integar to string for displaying the word to user as string
            word += char # appending the char (string number) to word (string variable)
            continue # continue the loop, the get the next char for checking

        cipher_char = alphabet.index(char) # in this case, char is a letter, get its index in alphapet list saving it to cipher_char variable
        word += alphabet[cipher_char+shift] # appending shifted letter (got encoded by getting the letter that is after cipher_char by shift) to the word
        
    print(f"\nEncoded result> {word}\n===========================================================") # print the encoded word

def decode(user_word,shift):
    word = "" # creating a word variable
    for char in user_word:  # iterating through every char in user_word
        if char in symbols:
            word += char
            continue
        elif char == "'":
            word += "'"
            continue
            

        elif char.isdigit():
            if user_word[user_word.index(char)-1] == "-":
                char = (int(char)*-1) - shift
            else: 
                char = int(char) - shift # converting character (number) from string to integar with incrementing it by a shift
            char = str(char)
            word += char
            continue
        
        cipher_char = alphabet.index(char)
        word += alphabet[cipher_char-shift]
    print(f"\nDecoded result> {word}\n===========================================================")

if __name__ == "__main__":

    print(logo,"\n\n") # logo for the app
    # saving list of all english letters to alphabet
    while True: # infinit loop
        choice = str(input("[+] Enter 'encode' to encrypt, 'decode' to decrypt, 'exit' to exit:\n> ")).lower() # taking user's choice
        if choice == "encode" or choice == "encrypt": # if choice is encode or encrypt
            user_word, shift = get_user_input() # getting what user inputs (user_word for encryption, number of shifts for encryption)
            encode(user_word,shift) # calling function to encode the word with passing the word, alphapets, shift
        elif choice == "decode" or choice == "decrypt": # if choice is decode or decrypt
            user_word, shift = get_user_input() # getting what user inputs (user_word for encryption, number of shifts for encryption)
            decode(user_word,shift) # calling function to decode the word with passing the word, alphapets, shift
        elif choice == "exit" or choice == "quit" or choice == "q": # if user exits
            break # close the loop (close the app)
        else: # if unexpected value
            print("[-] Wrong Entry!\n===================================================================") 






    