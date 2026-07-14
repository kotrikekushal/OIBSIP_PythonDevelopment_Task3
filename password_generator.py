import tkinter as tk
import random
import string

generated_password = ""

def password_generator():
    global generated_password
    try:
        length = int(password_length_entry.get())
    except ValueError:
        result.config(text="Enter valid number")
        return
    if length <= 0:
        result.config(text="Length must be greater than 0")
        return

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation
    
    if not characters:
        result.config(
            text="Select at least one option"
        )
        return
    password = ""

    for i in range(length):
        password += random.choice(characters)
    
    result.config(text=f"password: {password}")
    generated_password = password

def clear_fields():
    password_length_entry.delete(0,tk.END)
    result.config(text="")

def copy_password():
    if not generated_password:
        result.config(
            text="Generate password first"
        )
        return

    window.clipboard_clear()
    window.clipboard_append(generated_password)
    result.config(text="Password copied to clipboard!")

window = tk.Tk()
window.title("Password Generator")
window.geometry("500x400")
window.resizable(False, False)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

title_label = tk.Label(window,text="Password Generator",font=("Arial",16,"bold"))
title_label.pack()

password_length = tk.Label(window,text="Password length")
password_length.pack()
password_length_entry = tk.Entry(window)
password_length_entry.pack()

letters_check = tk.Checkbutton(window,text="Letters",variable=letters_var)
letters_check.pack()
numbers_check = tk.Checkbutton(window,text="Numbers",variable=numbers_var)
numbers_check.pack()
symbols_check = tk.Checkbutton(window,text="Symbols",variable=symbols_var)
symbols_check.pack()
generate_password = tk.Button(window,text="Generate password",command=password_generator)
generate_password.pack(pady=5)

copy_button = tk.Button(window,text="Copy Password",command=copy_password)
copy_button.pack(pady=5)

result = tk.Label(window,text="")
result.pack()

clear_button = tk.Button(text="Clear",command=clear_fields)
clear_button.pack(pady=5)

window.mainloop()

