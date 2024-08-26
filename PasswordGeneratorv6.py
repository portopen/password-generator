#!/usr/bin/env python3

# This program creates a strong secure password

import string
import secrets
from tkinter import *
from tkinter import ttk # This is needed for the combo box

main_window = Tk()
main_window.title("Password Generator")
main_window.geometry("900x400")
main_window.maxsize(900, 400)
main_window.minsize(900, 400)

# Command for button one: generate strong password
def new_rand():
    if var.get() == 0:
        # Clear entry box
        pw_entry.delete(0, END)

        # Get password length and convert to integer
        pw_length = int(char_box.get())

        # create password
        alphabet = string.ascii_letters + string.digits
        # check if password contains atleast one upper, one lower and one digit
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
                break
        # Output password to screen
        pw_entry.insert(0, password)
    else:
        # Clear entry box
        pw_entry.delete(0, END)

        # Get password length and convert to integer
        pw_length = int(char_box.get())

        # create password
        spec = "!@#$%^&*"
        alphabet = string.ascii_letters + string.digits + spec
        # check if password contains atleast one upper, one lower and one digit and one special character
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in spec for c in password)):
                break
        # Output password to screen
        pw_entry.insert(0, password)


# Command for button two
def copytext():
    # Clear the clipboard
    main_window.clipboard_clear()
    # Copy to clipboard
    main_window.clipboard_append(pw_entry.get())

# Create a frame for widgets
frame_one = Frame(main_window)
frame_one.pack(pady=40)
#Label Frame
lab_one = Label(frame_one, text="Select length of password:", font=("Helvetica", 18))
lab_one.grid(row=0, column=0)

# create a combo box
options = ['12', '13', '14', '15', '16', '17', '18','19', '20', '21', '22', '23', '24']
char_box = ttk.Combobox(frame_one, value=options, width=6, font=("Helvetica", 18))
char_box['state'] = 'readonly'
char_box.grid(row=0, column=1, padx=10)
# Show twelve as a default value
char_box.current(0)

#create a frame for widgets
frame_two = Frame(main_window)
frame_two.pack()

# create text for checkbox
lab_two = Label(frame_two, text="Include special characters:", font=("Helvetica", 18))
lab_two.grid(row=0, column=0)

# change blue highlight of checkbox to no highlight
style = ttk.Style()
style.configure('TCombobox', selectbackground="gray85", selectforeground="black")

# Create checkbox
var = IntVar()
check_box = Checkbutton(frame_two, variable=var, font=("Helvetica", 24), offvalue=0, onvalue=1)
check_box.deselect()
check_box.grid(row=0, column=1)

#Entry Box for returned password
# setting the bg to "gray85" makes the Entry box seem invisible
pw_entry = Entry(main_window, text="", width=30, font=("Helvetica", 20))
pw_entry.pack(pady=40)

# Create a frame for buttons
frame_three = Frame(main_window)
frame_three.pack(pady=20)

#Create our buttons
button_one = Button(frame_three, text="Generate Password", font=("Helvetica", 16), command=new_rand)
button_one.grid(row=0, column=0, padx=10)

button_two = Button(frame_three, text="Copy to Clipboard", font=("Helvetica", 16), command=copytext)
button_two.grid(row=0, column=1, padx=10)


main_window.mainloop()
