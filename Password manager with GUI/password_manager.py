from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

def find_password():
    search = website_entry.get().title()
    try:
        with open("My_passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="NO data file found")
    else:
        for web in data:
            if web == search:
                s_data = data[search]
                s_email = s_data["Email/username"]
                s_pass = s_data["Password"]
                pyperclip.copy(s_pass)
                messagebox.showinfo(title="Here's your password", message=f"Email: {s_email}\nPassword: {s_pass} \n\n Your password is automatically copied.\nJust paste where you want to paste it!")      
            else:
                messagebox.showinfo(title="Error", message=f"No details for {search} exists")


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(END, f"{password}")
    pyperclip.copy(password)


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = pass_entry.get()
    manage = {
        website: {
            "Email/username": email,
            "Password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) ==0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="You left some of the box Empy.\n Please Fill all of them")
    elif len(password) < 8:
        messagebox.showinfo(title="Password Error", message="Your Password is less than eight character?")
    else:
        ok_everything = messagebox.askokcancel(title=f"Details for {website}", message=f"Your Email is : {email} \n Password is : {password} \n Do You Want to Save?")

        if ok_everything:
            try:
                #Checking if my_password.json exists or not.
                with open("My_passwords.json") as pass_mng:
                    data = json.load(pass_mng)
            #If there is no my_password.json file then create one.
            except FileNotFoundError:
                with open("My_passwords.json", mode="w") as pass_mng:
                    json.dump(manage, pass_mng, indent=4)
            else:
                #Check IF Email and Passwords alereay exists
                if website in data and data[website]["Email/username"] == email:
                    messagebox.showinfo(title="Error", message="That Same Email and Website aleady exists. \n Either change email or website.")
                else:
                    data.update(manage)
                    with open("My_passwords.json", "w") as pass_mng:
                        json.dump(data, pass_mng, indent=4)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


window = Tk()
window.title("My Password Manager!")
window.config(padx=75, pady=60)

canvas = Canvas(width=200, height=200)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "wrilka76@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", command=generate_pass, bg="lightgreen")
generate_pass_button.grid(column=2, row=3, padx=4)
add_button = Button(text="Add", width=45, command=save, bg="yellow")
add_button.grid(column=1, row=4, columnspan=2, pady=3)
search_button = Button(text="Search", width=15, bg="pink", command=find_password)
search_button.grid(column=2, row=1)







window.mainloop()