import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

# keeps the game running with a "tick" ever 0.1 second
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car(scoreboard.level)
    car_manager.move_cars()

    # Checks if the player has finished the level
    if player.check_if_at_finishline():
        player.reset()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # checks if the player has been hit by a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()



