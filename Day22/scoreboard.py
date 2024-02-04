from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.write_score()

    def r_increase_score(self):
        self.clear()
        self.r_score += 1
        self.write_score()

    def l_increase_score(self):
        self.clear()
        self.l_score += 1
        self.write_score()

    def write_score(self):
        self.write(arg=f"{self.r_score} || {self.l_score}"\
                   , move = False, align = ALIGNMENT, font = FONT)