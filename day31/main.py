import random
from tkinter import *

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


try:
    word_dict = pd.read_csv("data/words_to_learn.csv").to_dict()
except FileNotFoundError:
    word_dict = pd.read_csv("data/french_words.csv").to_dict()

flip_action_timer = None
random_index = None
prev_index = []


def word_in_english():
    canvas.itemconfig(canvas_image, image=card_back)
    english_word = word_dict["English"][random_index]
    canvas.itemconfig(language_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=english_word)


def words_to_learn():
    data = pd.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


def word_in_french():
    canvas.itemconfig(canvas_image, image=card_front)
    french_word = word_dict["French"][random_index]
    canvas.itemconfig(language_text, fill="black", text="French")
    canvas.itemconfig(word_text, fill="black", text=french_word)


def button_click(remove):
    global flip_action_timer, random_index
    if remove:
        del(word_dict["French"][random_index])
        del(word_dict["English"][random_index])
    if flip_action_timer is not None:
        window.after_cancel(flip_action_timer)
    random_index = random.randint(0, len(word_dict["French"]))
    while random_index in prev_index:
        random_index = random.randint(0, len(word_dict["French"]))
    word_in_french()
    flip_action_timer = window.after(3000, word_in_english)
    prev_index.append(random_index)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Trauve", fill="black", font=("Ariel", 60, "bold"))

correct_btn_image = PhotoImage(file="images/right.png")
correct_btn = Button(image=correct_btn_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: button_click(True))
correct_btn.grid(row=1, column=0)

wrong_btn_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: button_click(False))
wrong_btn.grid(row=1, column=1)

button_click(None)

window.mainloop()

words_to_learn()
