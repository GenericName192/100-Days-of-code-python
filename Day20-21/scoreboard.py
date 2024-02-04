from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(arg=f"score: {self.score}", move = False, align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER \nFinal score: {self.score}", move = False, align = ALIGNMENT, font = FONT)