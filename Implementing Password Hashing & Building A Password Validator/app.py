from tkinter import *
import bcrypt

root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="validate", 
                command=lambda: validate(password_entry.get()))
button.pack()


root.mainloop()