import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Hruban Crossing_game")
screen.tracer(0)
screen.listen()

turtle = Player()
scoreboard = Scoreboard()
car_list = []
for car in range(25):
    car = CarManager()
    car_list.append(car)



screen.onkeypress(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    for cars in car_list:
        cars.move_refresh()
        #detect colision with car
        if turtle.distance(cars) < 25:
            scoreboard.game_over()
            game_is_on = False


    #detect finish_line
    if turtle.finish():
        scoreboard.level_up()
        for cars in car_list:
            cars.increase_speed()


screen.exitonclick()