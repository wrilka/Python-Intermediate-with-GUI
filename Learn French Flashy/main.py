from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
dict_word = {}
to_learn ={}

try:
    data = pandas.read_csv("data/need_to_learn.csv")
except:
    off_data = pandas.read_csv("data/french_words.csv")
    to_learn = off_data.to_dict(orient="records")
    print(to_learn)
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global dict_word, flip_timer
    window.after_cancel(flip_timer)
    dict_word = random.choice(to_learn)
    canvas.itemconfig(title_que, text="French", fill="black")
    canvas.itemconfig(word_que, text=dict_word["French"], fill="black")
    canvas.itemconfig(front_card, image=front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_que, text="English", fill="white")
    canvas.itemconfig(word_que, text=dict_word["English"], fill="white")
    canvas.itemconfig(front_card, image=back_image)


def i_know():
    to_learn.remove(dict_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/need_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
front_card = canvas.create_image(400, 263, image=front_img)
title_que = canvas.create_text(400, 150, text="Title", font=("Arial", 50, "italic"))
word_que = canvas.create_text(400, 260, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=1, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=1, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=i_know)
right_button.grid(column=2, row=1)

next_card()

window.mainloop()