from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_bg, image=card_b_img)


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    try:
        current_card = random.choice(to_learn)
    except IndexError:
        raise EXCEPTION("Congratz, you have learned all the words.")

    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_bg, image=card_f_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    try:
        to_learn.remove(current_card)
    except ValueError or IndexError:
        raise EXCEPTION("Congratz, you have learned all the words.")

    data_to_save = pandas.DataFrame(to_learn)
    data_to_save.to_csv('data/words_to_learn.csv', index=False)
    print(len(to_learn))
    next_card()


try:
    data = pd.read_csv("data/words_to_learn.csv")
# in case we run the program for the first time and we don't have the file to open
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
# in case we closed the problems after we have finished all the words
except pandas.errors.EmptyDataError:
    raise EXCEPTION("Congratz, you have learned all the words, take a rest rn.")
else:
    to_learn = data.to_dict(orient='records')

window = Tk()
window.title("Flash bang")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526)

card_f_img = PhotoImage(file='images/card_front.png')
card_b_img = PhotoImage(file='images/card_back.png')
card_bg = canvas.create_image(400, 263, image=card_f_img)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
cross_image = PhotoImage(file='images/wrong.png')
idk_button = Button(image=cross_image, highlightthickness=0, command=next_card)
idk_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
ikr_button = Button(image=check_image, highlightthickness=0, command=is_known)
ikr_button.grid(row=1, column=1)

next_card()

window.mainloop()
