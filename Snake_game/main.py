from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time#pt delay-ul de dupa update la imagine

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hruban Snake")
#tracer(0)(opreste animatiile), merge cu update() = da update la imagine, se genereaza instant
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()#PT SCREEN.ONKEY
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()#faci update la imagine dupa ce se muta toate 3 bodys!!
    time.sleep(0.08) #faci delay la refresh ca sa controlam cand se inatmpla ,fara delay imi nu apuc sa vad pe ecran
    snake.move()

    #detect collisions with food
    if snake.head.distance(food) < 20:#alegi tu un nr (20 e okay)
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    #detect collision with tail cu slicing!

    for body in snake.body_list[1:]:   #fara snake.head
        if snake.head.distance(body) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()





screen.exitonclick()