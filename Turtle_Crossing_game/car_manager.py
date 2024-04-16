from turtle import Turtle, back
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 0.5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(self.rand_color())
        self.starting_pos()
        self.move_speed = STARTING_MOVE_DISTANCE


    def rand_color(self):
        rand_int = random.randint(0,5)
        return COLORS[rand_int]
    
    def starting_pos(self):
        self.goto(self.rand_starting_pos())
    
    def rand_starting_pos(self):
        x = random.randint(320, 1000)
        y = random.randint(-240, 240)
        return (x,y)
    
    def move_back(self):
        self.back(self.move_speed)

    def refresh(self):
        if self.xcor() <= -320:
            self.starting_pos()

    def move_refresh(self):
        self.move_back()
        self.refresh()

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT