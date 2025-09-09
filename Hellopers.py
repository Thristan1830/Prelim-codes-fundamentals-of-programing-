import random
secret_number = 15
print("welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")
while True:
    try:
        guess = int(input("enter your guess:"))
        if guess  < secret_number:
            print ("too low! Try Again")
        elif guess > secret_number:
            print("Too High! Try Again")
        else:
            print("You are awesome! you guessed it right!")
            break
    except ValueError:
        print("please enter a valid number")