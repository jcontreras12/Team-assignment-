#Jose Contreras
# Date 11/2/21
#
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
