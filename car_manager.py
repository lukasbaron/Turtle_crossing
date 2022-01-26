from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITION_Y = [-280, -260]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.new_increment = 0
        self.all_cars = []

    def car_creator(self):
        random_choice = random.randint(1, 6)
        if random_choice == 2:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.hideturtle()
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.setposition(320, rand_y)
            new_car.showturtle()
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.new_increment)

    def level_up(self):
        self.new_increment += MOVE_INCREMENT

