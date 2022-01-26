import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle race")
screen.listen()

screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
scoreboard.update_level()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_creator()
    car_manager.move()

    if player.ycor() > 270:
        scoreboard.add_point()
        player.finish()
        car_manager.level_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            player.collision()
            game_is_on = False

    screen.update()
screen.exitonclick()
