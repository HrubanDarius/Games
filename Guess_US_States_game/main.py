from random import gammavariate
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("Guess US States!")
screen.setup(height=491, width=725)#dim pozei

#Asa adaugi imagini
image = "./FullCourse/25_Guess_States_game/blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(shape=image)

data = pandas.read_csv("./FullCourse/25_Guess_States_game/50_states.csv")
states = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

correct_count = 0
game_is_on = True
while game_is_on:
    if correct_count == 50:
        break
        
    answer_text = screen.textinput(title=f"{correct_count}/50 States Correct", prompt="What's another state's name:").lower()
    if answer_text.lower() == "exit":
        break

    for i in range(len(states)):
        if states[i].lower() == answer_text:
            turtle_aux = Turtle()
            turtle_aux.hideturtle()
            turtle_aux.penup()
            turtle_aux.goto(x=x_list[i], y=y_list[i])
            turtle_aux.write(states[i], align= "Center",font= ("Arial",10,"normal"))
            correct_count += 1
        

#saving data not guessed at final..
