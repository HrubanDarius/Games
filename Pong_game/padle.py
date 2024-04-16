from turtle import Turtle, xcor
UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

class Padle(Turtle):
    def __init__(self, size):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(size)
    

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(),y=new_y)
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y= new_y)