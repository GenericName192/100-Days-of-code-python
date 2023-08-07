import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

endOfGame = False
wordList = ["ardvark", "baboon", "camel"]
chosenWord = random.choice(wordList)
wordLength = len(chosenWord)

lives = 6


display = []
for _ in range(wordLength):
    display += "_"

while not endOfGame:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}, you already know its in the word, try again")

    else:
        for position in range(wordLength):
            letter = chosenWord[position]

            if letter == guess:
                display[position] = letter


        if guess not in chosenWord:
            print(f"You guessed wrong, {guess} is not in the word. You lose a life")
            lives -= 1
            if lives == 0:
                endOfGame = True
                print("You have run out of lives, you lose!")


        print(f"{' '.join(display)}")


        if "_" not in display:
            endOfGame = True
            print("You win! You saved your friend")

        print(stages[lives])