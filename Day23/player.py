from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Class for the player or "turtle"
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.tilt(90)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

    # Allows the player to move forward.
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    # checks if the player has reached the end
    def check_if_at_finishline(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        
    # resets the player position at the start of the level
    def reset(self):
        self.goto(STARTING_POSITION)