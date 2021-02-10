# this calculator app, calculates arthimitc operations with features of:
# 1 - asking user whether he wants to continue operations on last result
# 2 - asking user whether he wants an approximate result (for float results) and how many rounds (numbers after . like 1.15151) he wants
from arts import logo
import os

def add(n1,n2):
    """Returns addition result of given numbers"""
    return n1+n2

def subtract(n1,n2):
    """Returns Subtraction result of given numbers"""
    return n1-n2

def multiply(n1,n2):
    """Returns Multiplication result of given numbers"""
    return n1*n2

def divide(n1,n2):
    """Returns Division result of given numbers"""
    if n2 == 0: # numbers cannot be divisible by 0
        return f"Second number can't be equal to 0\nReloading ....\n==========================================="
    return n1/n2



def calculate(operations): 
    """Enables to make calculations on numbers, choosing specific approximations, and on result numbers if user wants to"""
    while True: # infinit loop
        approximate_choice = str(input("do you want to get approximate result? (y/n)\n> ")) # asking whether a user wants an approximate result?
        approximate_rounds = int(input("How many numbers you want for approximation? (for example: if 2 numbers > (result > 4.78) )\n> ")) # explained in message
        if approximate_choice == "y" and approximate_rounds == int(approximate_rounds): # checing if user's choice is yes and if the given rounds is integar number
            approximate = True # defining a boolean variable set to True
            break # break the current loop
        elif approximate_choice == "n": # if choice is no
            approximate = False # defining approximate set to False
            break # break the current loop
        else: # if unexpected inputs
            print("Please Enter 'y' or 'n', and make sure that you entered an integar number for approximation!\n===============================================")
        


    os.system("clear")
    answer = "" # result message for user
    result_continue = False # boolean variable indicates whether a user wants to make other operations on result of operation
    while True: # infinit loop
        try: # using try, in case if user gives a different input instead of float or int for num1 and num2
            if result_continue: # if user chose to make another operations on the result
                num1 = answer # num1 will be equal to the answer which holds the operation result
            else: # if not
                num1 = float(input("[+] What's the first number?\n> ")) # app will ask user for a number when app start.
            
            for op in operations:
                """Displaying operations for user to choose"""
                print(f"{op}")
            op_sym = input("[+] Pick an operation:\n> ") # asking user to choose an operation
            num2 = float(input("[+] What's the second number?\n> ")) # asking user to input the second number
            answer = operations[op_sym](num1,num2) # calling the function with passing numbers to it and saving its return to answer variable
            # operations is a dictionary, each key (operation) is equal to its function variable.
            # operations[op_sym] = the function variable, for example it's 'add', then > add(num1,num2)
        except: # if an error occurred due to user input
            print("[-] Invalid Input!") # display this message
            continue # reload the loop



        if num2 != 0: # making sure that num2 is not equal to 0
            if approximate:
                result = round(float(answer),approximate_rounds) # making an instance of answer with specific approximation
            # be carefull that num1 can equal to result (answer), if user accepted to make another operations on result of first operation
            # because we did num1 = answer above


            # the following checks are for ui and displaying the right types of numbers for user
            if num1 == int(num1) and num2 == int(num2): # if num1 and num2 are integars
                if result == int(answer): # if result is integar
                    print(f"{round(num1)} {op_sym} {round(num2)} = {round(answer)}") # display for example > 1 + 1 = 2
                    result = int(result) # converting result from float to integar
                else: # if result is not integar
                    print(f"{round(num1)} {op_sym} {round(num2)} = {round(answer,approximate_rounds)}") # display for example > 3 / 2 = 1.5


            # round(answer,approximate_rounds) is the result with specific approximation given by the user


            # remember that num1 can equal to result (answer) which may be float or int
            elif num1 == float(num1) and num2 == float(num2): # if num1 and num2 are float numbers
                if result == int(answer): # if result is integar
                    print(f"{num1} {op_sym} {num2} = {round(result)}") # display for example > 1.5 + 2.5 = 4
                    result = int(result)
                else: # if result is not integar 
                    print(f"{num1} {op_sym} {num2} = {round(result,approximate_rounds)}") # display for example > 1.2 + 3.5 = 4.7




            # remember that num1 can equal to result (answer) which may be float or int
            elif num1 == int(num1) or num2 == int(num2): # if  num1 is int or num2 is int
                if approximate:
                    if num1 == int(num1): # if num1 is int
                        print(f"{round(num1)} {op_sym} {num2} = {round(answer,approximate_rounds)}") # display for example > 4 + 2.5 = 6.5
                    elif num2 == int(num2): # if num2 is int
                        print(f"{num1} {op_sym} {round(num2)} = {round(answer,approximate_rounds)}") # display for example > 2.5 + 4 = 6.5
                    
                if result == int(answer): # if result is int
                    result = int(result) # set it to integar number



            # remember that num1 can equal to result (answer) which may be float or int
            elif num1 == float(num1) or num2 == float(num2): # if num1 is float or num2 is float, num1 may be equal to last result
                if approximate:
                    if num1 == float(num1): # if num1 is float
                        print(f"{num1} {op_sym} {round(num2)} = {round(answer,approximate_rounds)}") # display for example > 2.5 + 3 = 5.5
                    elif num2 == float(num2): # if num2 is float
                        print(f"{round(num1)} {op_sym} {num2} = {round(answer,approximate_rounds)}") # display for example > 3 + 2.5 = 5.5
                
                if result == int(answer): # if result is integar
                    result = int(result) # set it to integar




            # after all checks above about types of variables, in the next message of choice, {result} will contain the right value type (float or int) for all cases.
            choice = str(input(f"[+] Do operations on same result {result}? (y/n)\n> ")) # asking user if he wants to make another operation on result (answer)
            if choice == "y": # if yes
                result_continue = True # set result_continue to True, which has checks above 
                os.system("clear")

            elif choice == "n": # if no
                break # close the loop, the user will be asked for '[+] Calculate? (y/n):\n> ' as in first while loop below

            else: # if any other different input
                print("[-] Wrong Entry!\n===================================================================")

        elif num2 == 0: # if num2 result from try except is = 0, we make a check, so now 'answer' contains the message we set in the divide function above
            print(f"{answer}") # displaying the message.

if __name__ == "__main__":
    print(f"{logo}\n") # a logo for the app
    operations = { # calculator operations
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide,
    } 
    
    while True: # infinit loop
        user_choice = str(input("[+] Calculate? (y/n):\n> ")) # asking user whether want to calculate something or not
        if user_choice == "y": # if yes
            calculate(operations) # call calculate function with passing 'operations'

        elif user_choice == "n": # if no
            break # close the app

        else: # if strange input
            print("[-] Wrong Entry!") # displaying this message and loop reloads
