import random
import os


def isValidInput(input, *arg):
    """Function thats takes in a user input and any number of valid answers and 
    returns True if the answer matches a valid input and False if it doesnt"""
    isValid = False
    for validInput in arg:
        if input == validInput:
            isValid = True
    return isValid

def guessNumberGame():
    """ Function that allows the player to play a number guessing game, spits out
    a number between 1 and 100 and lets the user try guess it."""
    number = random.randint(1,100)
    print("Welcome to the number guessing game \n I am thinking of a number between 1 and 100")
    print(f"pst.. its {number}")
    validDifficulty = False
    while not validDifficulty:
        difficulty = input("Choose a difficulty, type (easy) or (hard) \n").lower()
        if isValidInput(difficulty, "easy", "hard"):
            validDifficulty = True
        else:
            print("Invalid input, try again.")
    if difficulty == "hard":
        lives = 5
    else:
        lives = 10
    while lives > 0:
        guess = int(input(f"You have {lives} left, guess a number between 1 and 100 \n"))
        if guess == number:
            print(f"You guessed correct the number was {number}, you win!")
            return
        elif guess > 100 or guess < 0:
            print("Invalid guess, lose a life")
            lives -= 1
        elif guess > number:
            print("You guessed too high, try again")
            lives -= 1
        else:
            print("You guessed too low, try again")
            lives -= 1
    print("You have run out of lives, you lose.")


playing = True
while playing:
    guessNumberGame()
    validAnswer = False
    while not validAnswer:
        playAgain = input(f"Would you like to play again? (yes), (no) \n").lower()
        if isValidInput(playAgain, "yes", "no"):
            validAnswer = True
        else:
            print("Invalid input, try again.")
    if playAgain == "no":
        playing = False
    os.system("cls")

