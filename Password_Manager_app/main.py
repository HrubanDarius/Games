from tkinter import *
from tkinter import messagebox
from pass_generator import pass_gen
import pyperclip#copiere clipboard la generate pass
import json
#Constante

STARTING_EMAIL = "my_email@yahoo.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    password = pass_gen()
    pass_entry.delete(0,END)
    pass_entry.insert(index=END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("./FullCourse/29_Password_manager/data.txt",mode="a") as data:
        web = web_entry.get()#ce ai in web_entry cu .get()!!!!!
        email = email_entry.get()
        pas = pass_entry.get()

        #MESSAGE BOX : from tkinter import messagebox(trebuie importat pt ca nu e o clasa din tkinter)
        if len(web) == 0 or len(email) == 0 or len(pas) == 0:
            print("Error")
            messagebox.showerror(title="Oops, error!", message="Hey, don't leave some fields empty!")

        else:
            answer = messagebox.askokcancel(title=f"Website: {web}", message=f"Details introduced:\nEmail: {email}\nPassword: {pas}\nIt's okay to save?")
            if answer == True:
                data.write(f"{web} | {email} | {pas}\n")

                web_entry.delete(0,END)
                pass_entry.delete(0,END)
                web_entry.focus()


# --------------------------- SAVE WITH JSON DATA FORMAT(import json)--------------------------------- #

def save_json():
    web = web_entry.get()
    email = email_entry.get()
    pas = pass_entry.get()

#----Cream DICTIONAR pt json.dump()------
    new_data = {
        web: {
            "email": email,
            "password": pas,
        }
    }
# ----------------------------------------
    if len(web) == 0 or len(email) == 0 or len(pas) == 0:
        messagebox.showerror(title="error", message="Hey, don't leave some fields empty!")
    else:
        answer = messagebox.askokcancel(title=f"Website: {web}", message=f"Details introduced:\nEmail: {email}\nPassword: {pas}\nIt's okay to save?")
        if answer == True:
        # ------------- UPDATE LA DATA JSON  --------------------
            try:
                with open("./FullCourse/29_Password_manager/data.json",mode="r") as data:
                    data_json = json.load(data)
                    data_json.update(new_data)
            except FileNotFoundError:
                with open("./FullCourse/29_Password_manager/data.json",mode="w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                with open("./FullCourse/29_Password_manager/data.json",mode="w") as data:
                    json.dump(data_json, data, indent=4) # ----- indent = 4 (nr de spatii de indentare la salvare)

            finally:
                web_entry.delete(0,END)
                pass_entry.delete(0,END)
                web_entry.focus()

# ---------------------------- SEARCH DATA WITH JSON ------------------ #
def search_data():
    web = web_entry.get()

    try:
        with open("./FullCourse/29_Password_manager/data.json",mode="r") as data:
            data_json = json.load(data)
    except FileNotFoundError:
            messagebox.showerror(title="Data empty!", message="Data was not saved until now!")
    else:
        ok = False
        for site_web in data_json:
            if site_web.lower() == web.lower():
                email = data_json[site_web]["email"]
                password = data_json[site_web]["password"]
                messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
                ok = True
        if ok == False:
            messagebox.showwarning(title="Webiste not found!", message="Try checking the website name again\nor add it if you did not do it yet!")

    finally:
        web_entry.delete(0,END)
        web_entry.focus()




# ---------------------------- UI SETUP ------------------------------- #

#screen
screen = Tk()
screen.config(padx=70, pady=50)
screen.title("Password Manager")

#image
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="./FullCourse/29_Password_manager/logo.png")
canvas.create_image(100,100, image=lock_image)

canvas.grid(row=0,column=1)

#Labels

website_label = Label(text="Website:", font=("Arial",10,"bold"))
email_user_label = Label(text="Email/Username:", font=("Arial",10,"bold"))
password_label = Label(text="Password:", font=("Arial",10,"bold"))

website_label.grid(row=1, column=0)
email_user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

#Entry's
web_entry = Entry(width=35)
email_entry = Entry(width=35)
pass_entry = Entry(width=35)

web_entry.focus()#pune cursoru la open program
email_entry.insert(index=END, string=STARTING_EMAIL)

web_entry.grid(row=1, column=1, columnspan=2)#columspan, EXTINDE pe 2 coloane..
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry.grid(row=3, column=1, columnspan=2)

#Buttons

search = Button(text="Search",width=15,command=search_data)
gen_pass = Button(text="Generate Password",width=15, command=password_gen)
add = Button(text="Add",width=30, command=save_json)

search.grid(row=1, column=3)
gen_pass.grid(row=3, column=3)
add.grid(row=4, column=1, columnspan=2)


screen.mainloop()
