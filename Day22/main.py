from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

speed = 0.1
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
score = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_running = True
while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect if the ball has hit a wall
    if ball.ycor() >= 290 or ball.ycor() <= - 290:
        ball.bounce_y()

    # detect if the ball has hit a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
        or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    # detect if l_paddle has missed the ball
    if ball.xcor() > 370:
        score.r_increase_score()
        ball.reset()

    # detect if r_paddle has missed the ball
    if ball.xcor() < -370:
        score.l_increase_score()
        ball.reset()

screen.exitonclick()