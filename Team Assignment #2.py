#Jose Contreras & Pedro Rodriguez
# Date 11/2/21
#import module 
#methord to generate random number between 1-10 
#print Please guessa number between 1-10
#Taking inputs 
#input if number is less than dice throw 
#print please guess higher
#print guess another number 
#input elif number is greater than dice throw 
#print plese guess lower 
#print guess another number
#if guess is correct break
#print Congratulations 

import random
diceThrow = random.randrange(1,11)
number = int(input("please guess a number between 1-10"))
while number != diceThrow:
    if number < diceThrow:
        print("Please guess higher")
    elif number > diceThrow:
        print("Please guess lower")
    number =int(input("Guess another number"))
print("Congratulations")
