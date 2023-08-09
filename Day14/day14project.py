import os
from art import logo, vs
from game_data import data
from random import randint

DATALENGTH = len(data)

def isValidInput(input, *arg):
    """Function thats takes in a user input and any number of valid answers and 
    returns True if the answer matches a valid input and False if it doesnt"""
    isValid = False
    for validInput in arg:
        if input == validInput:
            isValid = True
    return isValid

def pickChallenger(defender):
    """ Function that picks a a dictonary from data (a list of dictonaries)"""
    challengerPicked = False
    while not challengerPicked:
        challengerIndex = randint(0, DATALENGTH - 1) # minus one as index starts at 0
        challenger = data[challengerIndex]
        if challenger != defender:
            return challenger
        
def higherLowerGame():
    score = 0
    playingGame = True
    defender = pickChallenger({}) # need a defender for the first round
    print(logo)
    while playingGame:
        print(f"""We have {defender['name']} who is a {defender['description']} from {defender['country']} with {defender['follower_count']}""")
        print(vs)
        challenger = pickChallenger(defender)
        print(f"""{challenger['name']} who is a {challenger['description']} from {challenger['country']} \n""")
        print(f"psst the challenger has {challenger['follower_count']}\n")
        pickedPerson = False
        while not pickedPerson:
            choice = input(f"Who do you vote for? {defender['name']} (a) or {challenger['name']} (b)\n").lower()
            if isValidInput(choice, "a", "b"):
                pickedPerson = True
            else:
                print("Invalid choice, please try again\n")
        if choice == "a":
            if defender["follower_count"] > challenger["follower_count"]:
                score += 1
                print(f"Woo you got it right, your score is now {score}\n")
            else:
                print(f"Sorry you got the answer wrong, you lose with a score of {score}\n")
                playingGame = False
        else:
            if defender["follower_count"] < challenger["follower_count"]:
                defender = challenger
                score += 1
                print(f"Woo you got it right, your score is now {score}\n")
            else:
                print(f"Sorry you got the answer wrong, you lose with a score of {score}\n")
                playingGame = False
    print("Thanks for playing!\n")


playing = True
while playing:
    higherLowerGame()
    validAnswer = False
    while not validAnswer:
        playAgain = input(f"Would you like to play again? (yes), (no) \n").lower()
        if isValidInput(playAgain, "yes", "no"):
            validAnswer = True
        else:
            print("Invalid input, try again.\n")
    if playAgain == "no":
        playing = False
    os.system("cls")
