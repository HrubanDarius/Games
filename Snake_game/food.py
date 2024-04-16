from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__() 
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)#10 / 10 circle
        self.color("blue")
        self.speed("fastest")# sau 10
        random_x = random.randint(-280, 280) #pt ca screen e pe 600/600
        random_y = random.randint(-280, 280) #pt ca screen e pe 600/600
        self.goto(random_x,random_y)

    def refresh(self):
        random_x = random.randint(-280, 280) #pt ca screen e pe 600/600
        random_y = random.randint(-280, 280) #pt ca screen e pe 600/600
        self.goto(random_x,random_y)
