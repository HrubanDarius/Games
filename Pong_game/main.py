from turtle import Turtle, Screen, xcor
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard
import time #sa mutam bila mai incet in while(delay la while)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Hruban Pong")

screen.tracer(0)#fara animatii

r_padle = Padle((350,0))
l_padle = Padle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(fun=r_padle.move_up, key="Up")
screen.onkeypress(fun=r_padle.move_down, key="Down")
screen.onkeypress(fun=l_padle.move_up, key="w")
screen.onkeypress(fun=l_padle.move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with padle
    if ball.distance(r_padle) < 50 and ball.xcor() > 330 or ball.distance(l_padle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    
    #detect miss
    elif ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.increase_l_score()

    elif ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.increase_r_score()
    



screen.exitonclick()