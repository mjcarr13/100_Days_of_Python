BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

from tkinter import *
import random
import pandas

#read csv using pandas module as a dataframe
data = pandas.read_csv("./data/indonesian_words.csv")
#create dictionary from our dataframe using the orient perameter set to records
# to create a list of dictionaries in format [{'French': word, 'English', 'word'}]
to_learn = data.to_dict(orient="records")
current_card = []

# ---------------------------- PICK A CARD ------------------------------- #

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Indonesian", fill="black")
    canvas.itemconfig(card_word, text=current_card["Indonesian"], fill="black")
    canvas.itemconfig(card_background, image=CARD_FRONT_IMG)
    window.after(5000, func=flipcard)


# ---------------------------- FLIP CARD ------------------------------- #

def flipcard():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    print(current_card["English"])
    canvas.itemconfig(card_background, image=CARD_BACK_IMG)

# ---------------------------- REMOVE TICKED WORDS ------------------------------- #

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv")


# ---------------------------- UI SETUP ------------------------------- #

#initialise window from Tk() class
window = Tk()
#name window
window.title("Flashy")
#window padding
window.configure(padx=50, pady= 50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flipcard)

#initialise canvas object from Canvas() class, set height and width
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR,
                highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
#save image as variable to add to canvas using PhotoImage function
CARD_FRONT_IMG = PhotoImage(file="./images/card_front.png")
CARD_BACK_IMG = PhotoImage(file="./images/card_back.png")

#add image to canvas using create_image function, half size and width of
card_background = canvas.create_image(400, 264, image=CARD_FRONT_IMG)
#add canvas to window using grid (for now) at 1,0
canvas.grid(row=0, column=0, columnspan=2)
#add two text labels to our canvas
card_title = canvas.create_text(400, 150, text="Indonesian", font=(FONT_NAME, 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text=f"", font=(FONT_NAME, 60, "bold"), fill="black")

#add tick and cross buttons

tick_img = PhotoImage(file="./images/right.png")
tick = Button(image=tick_img, highlightthickness=0, bg=BACKGROUND_COLOR,
              highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=is_known)
tick.grid(row=1, column=0)

cross_img = PhotoImage(file="./images/wrong.png")
cross = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR,
              highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=next_card)
cross.grid(row=1, column=1)

next_card()

#keep whole thing running and listening using .mainloop on our window
window.mainloop()



