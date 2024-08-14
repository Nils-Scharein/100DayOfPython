import random
import tkinter as tk
from tkinter import ttk
import os
import pandas as pd
import pandas.errors

current_card = {}

# Defines
BACKGROUND_COLOR = "#B1DDC6"

# Tkinter window setup
window = tk.Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Paths to images
card_back_image = tk.PhotoImage(file="images/card_back.png")
card_front_image = tk.PhotoImage(file="images/card_front.png")
right_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")

# Canvas setup
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card_image = canvas.create_image(400, 263, image=card_front_image)  # Centered image
canvas_language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))  # Centered text
canvas_word_text = canvas.create_text(400, 263, text="Title", font=("Ariel", 40, "italic"))  # Centered text
canvas.grid(row=0, column=0, columnspan=2)  # Make canvas span across two columns

def unknown():
    global current_card
    nextCard()

def known():
    global current_card
    word_list.remove(current_card)
    wordsToLearn = pd.DataFrame.from_dict(word_list)
    wordsToLearn.to_csv("data/wordsToLearn.csv", index=False)
    nextCard()

def nextCard():
    global current_card
    current_card = random.choice(word_list)
    canvas.itemconfig(canvas_card_image, image=card_front_image)
    canvas.itemconfig(canvas_language_text, fill="black")
    canvas.itemconfig(canvas_language_text, text="French")
    canvas.itemconfig(canvas_word_text, fill="black")
    canvas.itemconfig(canvas_word_text, text=current_card["French"])
    window.after(3000, func=flipCard)

def flipCard():
    canvas.itemconfig(canvas_card_image, image=card_back_image)
    canvas.itemconfig(canvas_language_text, fill="white")
    canvas.itemconfig(canvas_language_text, text="English")
    canvas.itemconfig(canvas_word_text, fill="white")
    canvas.itemconfig(canvas_word_text, text=current_card["English"])

# Wrong button
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=unknown)
wrong_button.grid(row=1, column=0)  # Stick to the right of the left column

# Right button
right_button = tk.Button(image=right_image, highlightthickness=0, borderwidth=0, command=known)
right_button.grid(row=1, column=1)  # Stick to the left of the right column

# Configure grid columns for centering
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

try:
    # Read the CSV file without including the index
    data = pd.read_csv("data/wordsToLearn.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    data = pd.read_csv("data/french_words.csv")
    # Save the file without the index
    data.to_csv("data/wordsToLearn.csv", index=False)

# Convert the DataFrame to a list of dictionaries
word_list = data.to_dict(orient="records")
nextCard()

window.mainloop()
