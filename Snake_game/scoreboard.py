from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",20,"normal")

with open("./FullCourse/20_Snake_game/data.txt", mode="r") as file:
    highscore_file = int(file.read())



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.highscore = highscore_file
        self.goto(0, 270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align = ALIGNMENT, font = FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            highscore_file = self.score
            with open("./FullCourse/20_Snake_game/data.txt", mode="w") as file:
                file.write(str(highscore_file))
            self.highscore = highscore_file
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)