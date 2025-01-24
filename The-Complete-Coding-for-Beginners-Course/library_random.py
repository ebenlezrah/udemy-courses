# python random
import random

number = random.randint(1, 100)
guess = input("Guess a whole number between 1 and 100: ")
print("You guessed " + guess)
if number == guess:
    print("Congratulations, you guessed it! The number was " + str(number))
else:
    print("Sorry, you're wrong. The number was " + str(number))