from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-210,250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.goto(POSITION)
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write_score()
