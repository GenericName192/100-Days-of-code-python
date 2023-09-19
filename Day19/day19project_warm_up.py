from turtle import Turtle, Screen

terry = Turtle()
screen = Screen()

def move_forwards():
    terry.forward(10)

def move_backwards():
    terry.forward(-10)

def clear_screen():
    terry.home()
    terry.clear()

def turn_right():
    terry.right(5)

def turn_left():
    terry.left(5)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)

screen.exitonclick()