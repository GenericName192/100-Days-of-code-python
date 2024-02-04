from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


# class for displaying the score or "level"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.write_level()

    # changes the score to show that the level has gone up.
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write_level()

    # writes out the level on the screen
    def write_level(self):
        self.write(arg=f"Level: {self.level}"\
                   , move = False, align = ALIGNMENT, font = FONT)

    # displays game over screen. 
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER \nFinal level: {self.level}", move = False, align = ALIGNMENT, font = FONT)
