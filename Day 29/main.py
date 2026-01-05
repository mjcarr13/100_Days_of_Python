#import all classes from tkinter
from tkinter import *
#import message box from tkinter
from tkinter import messagebox
#import random module for password generator
from random import choice, randint, shuffle
#import pyperclip to allow us to save password to clipboard
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    #refactor code below as single lines using list comprehension syntax:

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    #add together to create list of all characters, symbols and numbers
    password_list = password_letters + password_numbers + password_symbols

    #randomise the order of the elements in the list
    shuffle(password_list)

    #create the password as a string using .join with no spaces inbetween
    password = "".join(password_list)
    #delete the current contents of the password box
    pw_box.delete(0,"end")
    #insert the new password into the box
    pw_box.insert(0,string=f"{password}")
    #add password to the clipboard
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #


#function for searching password json
def search_password():
#save website from text box to variable
    site_to_check = website_box.get().title()
#try opening the json file in read mode and saving data as a dictionary to a new variable
    try:
        with open("data.json", mode="r") as data_file:
            json_data = json.load(data_file)
#if the site saved as a string from the website text box exists as a key in our dictionary
            if json_data[site_to_check]:
#then open a messagebox giving the email and password values from the dictionary under that site
                messagebox.showinfo(title=f"{site_to_check}", message=f"Email/Username: {json_data[site_to_check]["email"]}"
                                                                      f"\nPassword: {json_data[site_to_check]["password"]}")
#anticipate json file not existing yet, print error message if so
    except FileNotFoundError:
        messagebox.showinfo(title=f"Oops!", message="No Data File Found")
#anticipate website not existing in the dictionary, print message if so
    except KeyError:
        messagebox.showinfo(title=f"Oops!", message=f"No details for {site_to_check} exist")





# If yes, show a messagebox with the website's name and password.


# Catch an exception that might occur trying to access the data. json showing a messagebox with the text: "No Data File Found"



# If the user's website does not exist inside the data. json, show a messagebox that reads "No details for the website exists".





# ---------------------------- SAVE PASSWORD ------------------------------- #

#need to take inputs from the website, email/username and PW boxes
#save these to a text file when the user clicks the add button
#format     website | user | password
#clear the current box content when add it hit with delete function

#define save function
def save():
    #take data from boxes as variables using .get()
    website = website_box.get()
    email = email_username_box.get()
    password = pw_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password}
    }

    #add popup if any fields are empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    #if fields aren't empty, proceed
    else:
#some exception work here. We try to read the data from the existing json so we can maniupulate it as the variable data
        try:
            with open("data.json", mode="r") as data_file:
                #Read the old data
                data = json.load(data_file)
#if we don't have that file yet, we catch it with the FileNotFoundError, and create it, passing in the new data
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                #Updating the old data with new data
                data.update(new_data, data_file, indent=4)
#the else statement runs if the try block completed, and here we update the old contents with the new
        else:
            data.update(new_data)
#we then write this updated contents to the existing json file
            with open("data.json", mode = "w") as data_file:
                #Saving updated data
                json.dump(new_data, data_file, indent=4)
#we use finally because whatever happens, we want to clear the boxes.
        finally:
                #clear the box fields present other than username
                website_box.delete(0,"end")
                pw_box.delete(0, "end")




# ---------------------------- UI SETUP ------------------------------- #




#set up tkinter window
window = Tk()
#window name
window.title("Password Manager")
#window padding
window.configure(padx=50, pady= 50)

#create canvas object with width and height of 200*200
canvas = Canvas(width=200, height=200)
#save image as variable to add to canvas using PhotoImage function
pw_lock_img = PhotoImage(file="logo.png")
#add image to canvas using create_image function, half size and width of
canvas.create_image(100, 100,image=pw_lock_img)
#add canvas to window using grid (for now) at 1,0
canvas.grid(column=1,row=0)

#ADDING LABELS TO CORRECT GRID LOCATIONS

#WEBSITE ROW
#add website label at 0,1
website_label = Label()
website_label.grid(column=0, row=1, sticky='w')
website_label.configure(text="Website:")

#add website text box at 1,1, spanning two columns, width: 35. Add focus for cursor
website_box = Entry(width=21)
website_box.grid(column=1, row=1)
website_box.focus()

#add Search Password button at 2,1
search_button = Button(width=13)
search_button.grid(column = 2, row=1)
search_button.configure(text="Search", command=search_password)


#EMAIL/USERNAME ROW
#add Email/Username label at 0,2
email_username_label = Label()
email_username_label.grid(column=0, row=2)
email_username_label.configure(text="Email/Username:")

#email/username entry box at 1,2,  spanning two columns, width: 35, with email pre-populated
email_username_box = Entry(width=38)
email_username_box.grid(column=1, row=2, columnspan=2)
email_username_box.insert(0,"michaeljcarr13@gmail.com")

#PASSWORD ROW
#add Password label at 0,3
pw_label  = Label()
pw_label.grid(column=0, row=3, sticky='w')
pw_label.configure(text="Password:")

#add password text box at 1,3, width 21
pw_box = Entry(width=21)
pw_box.grid(column=1, row=3)

#add Generate Password button at 2,3
generate_pw_button = Button()
generate_pw_button.grid(column = 2, row=3)
generate_pw_button.configure(text="Generate Password", command=generate_pw)

#ADD ROW
#add "Add" button at 1,4, spanning two columns, width 36
add_button = Button(width=36)
add_button.grid(column = 1, row= 4, columnspan=2)
add_button.configure(text="Add", command=save)






#window loop
window.mainloop()


