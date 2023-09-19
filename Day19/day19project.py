from turtle import Turtle, Screen
import random


is_race_running = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", 
                            prompt="which color turtle will win the race?")

colors = ["red", "blue", "green", "purple", "yellow", "pink", "black", "grey"]

turles = []

for turle_index in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[turle_index])
    t.penup()
    t.goto(x=-240, y=( -len(colors) * 8 + turle_index * 20))
    turles.append(t)

if user_bet:
    is_race_running = True

while is_race_running:

    for turtle in turles:
        if turtle.xcor() >= 230:
            is_race_running = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! well done for picking {winning_color}")
            else:
                print(f"You lost! {winning_color} won, dont you feel silly for betting on {user_bet}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()