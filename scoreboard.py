from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.point = 1
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setposition(0, 260)

    def update_level(self):
        self.write(f"Level:{self.point} ", False, "center", FONT)

    def add_point(self):
        self.clear()
        self.point = self.point + 1
        self.update_level()
