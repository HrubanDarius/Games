from tkinter import *
import pandas
import random

#data e REALIZAT CU GOOGLE SHEETS si cu =GOOGLETRANSLATE..

#-----------------------Constante----------------------
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_list_dict = {}

try:
    data = pandas.read_csv("./FullCourse/31_Flash_card_project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./FullCourse/31_Flash_card_project/data/top500_engleza-romana.csv")
    data_list_dict = original_data.to_dict(orient="records")

else:
    data_list_dict = data.to_dict(orient="records") #Formateaza MULT MAI LEJER/ O LISTA DE DICTIONARE


#----------------------BUTTONS-------------------------

def next_card():
    global current_card
    global flip_timer
    screen.after_cancel(flip_timer)

    current_card = random.choice(data_list_dict)
    flash_canvas.itemconfig(title, text="Engleză", fill="black")
    flash_canvas.itemconfig(word, text=current_card["Engleza"], fill="black")
    flash_canvas.itemconfig(card_backround, image=card_front)
    flip_timer = screen.after(3000, func=flip_card)


def is_known():
    data_list_dict.remove(current_card)
    print(f"Mai ai {len(data_list_dict)} de cuvinte de retinut!")
    next_card()

    data_to_learn = pandas.DataFrame(data_list_dict)
    data_to_learn.to_csv("./FullCourse/31_Flash_card_project/data/words_to_learn.csv", index=False)
    
#---------------------FLIP-----------------------

def flip_card():
    flash_canvas.itemconfig(title, text="Română",fill="white")
    flash_canvas.itemconfig(word, text=current_card["Romana"], fill="white")
    flash_canvas.itemconfig(card_backround, image=card_back)

#------------------------GUI----------------------------

#screen
screen = Tk()
screen.minsize(width=800,height=600)
screen.maxsize(width=1000,height=800)
screen.config(padx=50, pady=50 ,bg=BACKGROUND_COLOR)
screen.title("învață engleză ușor!")

flip_timer = screen.after(3000, func=flip_card)


#image
flash_canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="./FullCourse/31_Flash_card_project/images/card_front.png")
card_back = PhotoImage(file="./FullCourse/31_Flash_card_project/images/card_back.png")
card_backround = flash_canvas.create_image(400,263,image=card_front)
title = flash_canvas.create_text(400,150, text="", fill="black", font=("Courier",30, "italic"))
word = flash_canvas.create_text(400,263, text="", fill="black", font=("Courier",35, "bold"))


right = PhotoImage(file="./FullCourse/31_Flash_card_project/images/right.png")
wrong = PhotoImage(file="./FullCourse/31_Flash_card_project/images/wrong.png")

flash_canvas.grid(row=0,column=0, columnspan=2)

#buttons
right_button = Button(image=right, highlightthickness=0,command=is_known)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)

right_button.grid(row=1,column=1)
wrong_button.grid(row=1,column=0)

next_card()#pt prima alegere

screen.mainloop()

