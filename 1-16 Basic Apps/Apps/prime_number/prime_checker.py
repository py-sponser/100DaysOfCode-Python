def prime_checker(num):
    """Check whether the number is prime or not"""
    is_prime = True # defning a boolean set to True
    for i in range(2,num): # iterating through numbers between 1 and the user's given number (from 2 to (user's number - 1))
        if num % i == 0: # if user's number accept division by any number between
            is_prime = False # the boolean set to False, which means that number is not prime

    if is_prime: # if True
        print("[+] Prime Number!") # prime number
    else: # if False 
        print("[+] Not a Prime Number!") # not a prime
        

number = int(input("[+] Enter a number> ")) # getting a number from user
prime_checker(num = number) # calling the prime_checker function with passing the user's given number
