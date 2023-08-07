import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def drawCard():
    """function for drawing 1 random card"""
    return cards[random.randint(0, len(cards) -1)] # minus one as the index starts at 0

def drawHand():
    """function for drawing 2 random cards"""
    cardOneIndex = drawCard()
    cardTwoIndex = drawCard()
    return [cards[cardOneIndex], cards[cardTwoIndex]]

def playGame():
    """Function for playing a text based game of blackjack"""
    playerCards = drawHand()
    computerCards = drawHand()
    computerTotal = sum(computerCards)
    playerTotal = sum(playerCards)
    print(f"""Your cards are {playerCards} for a total of {playerTotal} /n
The computer has a {computerCards[0]} and a face down card""")
    inGame = True
    while inGame:
        anotherCard = input("Would you like another card? (yes), (no) ").lower()
        if isValidInput(anotherCard, "yes", "no"):
            if anotherCard == "yes":
                playerCards.append(drawCard())
                playerTotal += playerCards[-1]
                print(f"You drew a {playerCards[-1]}, Your new total is {playerTotal}")
                if scoreChecker(playerTotal):
                    if 11 in playerCards:
                        playerCards[playerCards.index(11)] = 1
                        playerTotal = sum(playerCards)
                        if scoreChecker(playerTotal):
                            print(f"{playerTotal} is over 21 therefore you lose!")
                            inGame = False
            else:
                print(f"The computer has {computerCards} with a total of {computerTotal}")
                while computerTotal < 17:
                    print("The dealer must draw another card..")
                    computerCards.append(drawCard())
                    computerTotal += computerCards[-1]
                    if scoreChecker(computerTotal):
                        if 11 in computerCards:
                            computerCards[computerCards.index(11)] = 1
                            computerTotal = sum(computerCards)
                            if scoreChecker(computerTotal):
                                print(f"With a total of {computerTotal}, The computer goes bust")
                                inGame = False
                        return
                    else:
                        print(f"The dealer draw a {computerCards[-1]}, for a new total of {computerTotal}")
                print(f"The comptuer sticks with a total of {computerTotal}")
                if playerTotal == computerTotal:
                    print("The game is a draw")
                    inGame = False
                elif playerTotal > computerTotal:
                    print(f"The player wins with a total of {playerTotal}")
                    inGame = False
                else:
                    print(f"The computer wins with a total of {computerTotal}")
                    inGame = False

        else:
            print("You have inputted an invalid answer, exiting out of game.")
            playing = False
            return

def isValidInput(input, *arg):
    """Function thats takes in a user input and any number of valid answers and 
    returns True if the answer matches a valid input and False if it doesnt"""
    isValid = False
    for validInput in arg:
        if input == validInput:
            isValid = True
    return isValid

def scoreChecker(Score):
    """Function to take a score and return True if its over 21 and the person
    has gone bust, if not returns False"""
    if Score > 21:
        return True
    else:
        return False
    
playingGame = True
while playingGame:
    playGame()
    playAgain = input("Would you like to play again? (yes), (no) ")
    if isValidInput(playAgain, "yes", "no"):
        if playAgain == "no":
            playingGame = False
    else:
        print("Invalid input, ending game")
        playingGame = False
            