BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

from tkinter import *
import random
import pandas

# ------------------- CREATE FLASH CARDS FROM CSV --------------------- #

def random_word():
    try:
        words_data = pandas.read_csv("./data/words_to_learn.csv")


    except FileNotFoundError:
        #create csv which is a duplicate of existing CSV
        words_data = pandas.read_csv("./data/German Words.csv")
        with open("./data/words_to_learn.csv", "w") as word_file:
            words_data.to_csv("./data/words_to_learn.csv", index=False)
    finally:
        num_words_in_csv = len(words_data)
        german_words = words_data["German"].to_list()
        english_words = words_data["English"].to_list()
        #change canvas label to German
        canvas.itemconfig(language_label, text="German", fill="black")
        #Change canvas image to front card image
        canvas.itemconfig(canvas_image, image = CARD_FRONT_IMG)
        #pick a random word from the word lists using a random integer
        random_index = random.randint(0,num_words_in_csv)
        random_german_word = german_words[random_index]

        translation = english_words[random_index]
        #update the canvas label with the word
        canvas.itemconfig(current_word, text=f"{random_german_word}", fill="black")
        #after three seconds, run the flipcard function, passing in the translated word as an argument
        window.after(3000, flipcard, translation)
    return random_german_word


def random_word_tick():
    remove_guessed_word(random_word())

# -------------------------- FLIP THE CARDS --------------------------- #


def flipcard(english_translation):
    # Change canvas image to back card image
    canvas.itemconfig(canvas_image, image = CARD_BACK_IMG)
    #change canvas label to English
    canvas.itemconfig(language_label, text="English",fill="white")
    # update canvas label with translated word
    canvas.itemconfig(current_word, text=f"{english_translation}", fill="white")



# ------------------ CREATE NEW LIST MINUS CORRECTLY WORDS ------------------ #

# def remove_guessed_word(german_list, english_list, german_word, english_word):
#     german_list.remove(german_word)
#     english_list.remove(english_word)
# #overwrite the existing CSV with the updated list
#     words_to_write = [german_list, english_list]
#     with open("./data/words_to_learn.csv", 'w', newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow(["German", "English"])
#         writer.writerows(words_to_write)
#         for item1, item2 in zip(german_list, english_list):
#             writer.writerow([item1, item2])
#     random_word()

def remove_guessed_word(german_word):
    file_name = "./data/words_to_learn.csv"
    column_name = "German"
    value_to_remove = german_word
    df = pandas.read_csv(file_name)
    df = df[df[column_name] != value_to_remove]
    df.to_csv(file_name, index=False)





# ---------------------------- UI SETUP ------------------------------- #

#initialise window from Tk() class
window = Tk()
#name window
window.title("Flashy")
#window padding
window.configure(padx=50, pady= 50, bg=BACKGROUND_COLOR)

#initialise canvas object from Canvas() class, set height and width
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR,
                highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
#save image as variable to add to canvas using PhotoImage function
CARD_FRONT_IMG = PhotoImage(file="./images/card_front.png")
CARD_BACK_IMG = PhotoImage(file="./images/card_back.png")
#add image to canvas using create_image function, half size and width of
canvas_image = canvas.create_image(400, 264, image=CARD_FRONT_IMG)
#add canvas to window using grid (for now) at 1,0
canvas.grid(row=0, column=0, columnspan=2)
#add two text labels to our canvas
language_label = canvas.create_text(400, 150, text="German", font=(FONT_NAME, 40, "italic"), fill="black")
current_word = canvas.create_text(400, 263, text=f"", font=(FONT_NAME, 60, "bold"), fill="black")

#add tick and cross buttons

tick_img = PhotoImage(file="./images/right.png")
tick = Button(image=tick_img, highlightthickness=0, bg=BACKGROUND_COLOR,
              highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=random_word_tick)
tick.grid(row=1, column=0)

cross_img = PhotoImage(file="./images/wrong.png")
cross = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR,
              highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=random_word)
cross.grid(row=1, column=1)

random_word()


#keep whole thing running and listening using .mainloop on our window
window.mainloop()




