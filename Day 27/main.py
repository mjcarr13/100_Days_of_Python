from tkinter import *

#initialise new object from tkinter class TK()
window = Tk()

#give title to the window
window.title("My First GUI Program")
#set minimum size for the window
window.minsize(width=500, height= 300)

#Label class initialised from tkinter class Label()

#function for button click

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

#call the function using the command argument. Note lack of ()
button = Button(text = "Click Me", command = button_clicked)
button.grid(row= 1, column=1)

my_label = Label(text="I am a label!", font=("Helvetica", 25, "bold") )
#pack sets the label to the middle of the window
my_label.grid(column =0, row=0)

new_button = Button(text="New button")
button.grid(column=2, row = 0)


#we can access and change the text content for my_label:
#we can access it like a dictionary using square brackets
my_label["text"] = "New text"
#or using config()
my_label.config(text="Newer text")

#Buttons



#Entry

#initialise Entry class for an input
input = Entry(width=10)
#bring on screen using pack
input.grid(row=3, column=3)


#Text entry

# Spinbox

# Scale

# Checkbox

# Radiobutton

# Listbox

#initliases a while loop for the window, keeping it open
# and listening for user input. Needs to be at end of programme
window.mainloop()