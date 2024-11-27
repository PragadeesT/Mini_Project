import random
import string
from tkinter import *
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length")
        return

    if length < 6:
        messagebox.showerror("Error", "Password length should be at least 6 characters.")
        return

    # Collect selected options
    include_uppercase = upper_var.get()
    include_lowercase = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    if not (include_uppercase or include_lowercase or include_digits or include_special):
        messagebox.showerror("Error", "At least one character type must be selected.")
        return

    # Create the character pool based on selected options
    character_pool = ""
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    generated_password.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(generated_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Setting up the GUI
root = Tk()
root.title('Custom Password Generator')
root.geometry('400x400')
root.config(bg='#000000')
root.resizable(False, False)

title_label = Label(root, text="Password Generator", font="Arial 20 bold underline", bg='#FFFFFF', fg='black')
title_label.pack(pady=10)

length_label = Label(root, text="Enter Password Length:", font="Arial 12 bold", bg='#FFFFFF', fg='black')
length_label.pack(pady=5)

length_entry = Entry(root, font="Arial 12", bd=6, relief='ridge')
length_entry.pack(pady=5)
length_entry.focus_set()

# Checkboxes for options
upper_var = BooleanVar(value=True)
lower_var = BooleanVar(value=True)
digits_var = BooleanVar(value=True)
special_var = BooleanVar(value=True)

Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, bg='#FFFFFF').pack(anchor=W)
Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, bg='#FFFFFF').pack(anchor=W)
Checkbutton(root, text="Include Digits", variable=digits_var, bg='#FFFFFF').pack(anchor=W)
Checkbutton(root, text="Include Special Characters", variable=special_var, bg='#FFFFFF').pack(anchor=W)

generate_button = Button(root, text="Generate Password", font="Arial 12 bold", bg='#FFFFFF', fg='black', command=generate_password)
generate_button.pack(pady=10)

generated_password = StringVar()
password_entry = Entry(root, textvariable=generated_password, font="Arial 12", bd=6, relief='ridge', fg='#DC143C')
password_entry.pack(pady=5)

copy_button = Button(root, text="Copy to Clipboard", font="Arial 12 bold", bg='#FFFFFF', fg='black', command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()
