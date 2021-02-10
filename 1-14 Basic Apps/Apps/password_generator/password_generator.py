import random, os
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z'] # lowercase letters
uppercase_letters = ['A', 'B', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
'X', 'Y', 'Z'] # uppercase letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # numbers
symbols = ['!', "@",'#', '$', '%', "^", '&', '(', ')', '*', '+',"-",
           "_","+","/","|","?",">","<",";",":"] # symbols
while True:
    user_choice = input("[+] Make strong password? (y / n)\n> ")
    if user_choice == "y":
        try:
            lowercase_letters_no = int(input("[+] Quntity of lowercase letters = ")) # asking user how many lowercase letters he wants
            uppercase_letters_no = int(input("[+] Quntity of uppercase letters = ")) # asking user how many uppercase letters he wants
            numbers_no = int(input("[+] Quantity of numbers = ")) # asking user how many numbers he wants
            sym_no = int(input("[+] Quantity of symbols = ")) # asking user how many symbols he wants
        except:
            print("[-] Error, Make sure you entered a number.")
            continue

        password = "" # password variable

        for i in range(1,lowercase_letters_no+1):
            """appending random lowercase letters depending on how many a user wants"""
            password += random.choice(letters)

        for i in range(1,uppercase_letters_no+1):
            """appending random uppercase letters depending on how many a user wants"""
            password += random.choice(uppercase_letters)


        for i in range(1,numbers_no+1):
            """appending random numbers depending on how many a user wants"""
            password += random.choice(numbers)

        for i in range(1,sym_no+1):
            """appending random symbols depending on how many a user wants"""
            password += random.choice(symbols)


        powerfull_password = "".join(random.sample(password,k=len(password))) # using join method of strings that converts list to a string.
        # what will be converted to string is a sample of the random password prepared but with randomizing indexes of the string which makes it more random.
        # if random password is "password" > after making a randomized sample > "rpsasdow"
        os.system("clear")
        print(f"Generated Password: {powerfull_password}") # displaying the final password


    elif user_choice == "n":
        break
    else:
        print("[-] Wrong Entry!")
