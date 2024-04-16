from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
#Culorile din 'COLORHUNT' WEBSITE
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    #anulam afterul din countdown()
    screen.after_cancel(timer)
    #timer_text
    canvas.itemconfig(timer_text, text="00:00")
    #timer_label
    label.config(text="    Timer   ",fg=GREEN)
    #Checkmarks
    checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    long_b = LONG_BREAK_MIN * 60
    short_b = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        countdown(long_b)
        label.config(text=" Long Break!", fg=RED)

    elif reps % 2 == 0:
        countdown(short_b)
        label.config(text="Short Break!",fg=PINK)
    else:
        countdown(work_sec)
        label.config(text=" Work Time! ",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    "00:00"
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"

    #putem folosi timer_text ca numa fara sa l trimitem ca argument pt ca programul a ajuns la final inainte sa se execute apelul(), programul sta in scree.mainloop() si asculta modificari aduse pe parcurs , adica after
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = screen.after(1000, countdown, count-1)#after(nr de milisecunde pt care asteapta(listen),apelezeaza o functie, argumetele functiei respective)
    else:
        start_timer()

        bife = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            bife += "✔"

        checkmark.config(text=bife)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Time Tracker")
screen.config(padx=100, pady=50, bg=YELLOW)


#label
label = Label(text="    Timer   ", font=(FONT_NAME,35,"bold"),fg=GREEN, bg=YELLOW)#fg = culoarea scrisului, bg = culoare backround
checkmark = Label(text="", font=(FONT_NAME,15,"bold"),fg=GREEN, bg=YELLOW)
label.grid(row=0,column=1)
checkmark.grid(row=3, column=1)

#buttons
but_1 = Button(text="Start",bg=GREEN,activebackground=GREEN,highlightthickness=0,command=start_timer)#highlighttjines = bordura alba din jurul obiecului 
but_2 = Button(text="Reset",bg=GREEN,activebackground=GREEN,highlightthickness=0, command=reset_timer)
but_1.grid(row=2,column=0)
but_2.grid(row=2,column=2)

#add image:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./FullCourse/28_Time_Tracker_App_Tkinter/tomato.png")
canvas.create_image(100, 112, image=tomato_img)#coordonatele centrului(mijlocul)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))


canvas.grid(row=1,column=1)

screen.mainloop()