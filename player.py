from turtle import Turtle
from scoreboard import Scoreboard
scoreboard = Scoreboard()

FONT = ("Courier", 24, "normal")
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.left(90)
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.showturtle()
        self.xcor()

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def collision(self):
        self.write("Game over", False, "center", FONT)

    def finish(self):
        self.goto(STARTING_POSITION)
