# for reeborg's world maze

# built in functions from the website
def turn_left():
    pass

def at_goal():
    pass

def right_is_clear():
    pass

def front_is_clear():
    pass

def move():
    pass

# my code
def turnRight():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turnRight()
    elif front_is_clear():
        move()
    else: 
        turn_left()