from turtle import Turtle, Screen
import math
import random
import turtle

# I'm not happy with how I did this task but I decided to keep it the way it was
# just as a reminder of my bad habbit of overcomplicating things.


turtle.colormode(255) 
screen = Screen()
terry = Turtle()
terry.shape("turtle")
terry.speed("fastest")
terry.penup()
terry.hideturtle()
colors = [(225, 134, 71), (154, 98, 28), (44, 106, 149), (18, 36, 57), (237, 80, 95), (222, 214, 3)]

dots_per_row = math.floor((screen.window_width() - 100) / 50)
num_of_rows = math.floor((screen.window_height() - 100) / 50)

for x in range(num_of_rows):
    terry.setx((screen.window_width() / 2 - 50) * -1)
    terry.sety(screen.window_height() / 2 - (50 * (x + 1)))

    for x in range(dots_per_row + 1):
        terry.dot(20, random.choice(colors))
        terry.forward(50)
    

screen.exitonclick()