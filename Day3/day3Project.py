print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('Do you go "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()

  if choice2 == "wait":
    choice3 = input('You get across unharmed and find yourself faced with 3 doors. One "red", one "yellow" and one "blue". Which colour do you choose? \n').lower()

    if choice3 == "red":
      print("red = dead. Game Over.")

    elif choice3 == "yellow":
      print("You dont want to know... Game Over.")

    elif choice3 == "blue":
      print("You found the treasure! You Win!")

    else:
      print("refusing to go through a door eh? well... Game Over.")

  elif choice2 == "swim":
    print("Sea monsters my guy, what were you thinking?. Game Over.")

  else:
    print("Refusing to answer eh? well then you get distracted by a bird and while distracted bad things happen. Game Over")

elif choice1 == "right":
  print("Your quest is so right you can no longer go left, you are doomed to walk right forever. Game Over")

else: 
  print("While thinking about it you randomly get hit by a bus. Game Over")