# code to create a Python Script that generates a secure and unique password
import string
import secrets
import tkinter as Tk
from tkinter import *
# importing a few modules to help with the build of this password generator
# string module used to grab all letters, numbers and symbols needed for our password
# secrets module use to generate cryptographically safe passwords, which adds a little bit of extra security to our generated password
# tkinter module used to create the GUI window for the user

# this is the function that is going to generate our password, relatively small I know, but I wanted to keep this simple

def BrickWall():
    global a1
    a1.set("")
    Length = int(b1.get())
    characters = string.printable
    password = "".join(secrets.choice(characters) for i in range(0, Length))
    a1.set(password)

# the GUI code for the user to see when running the script, instead of using the terminal
Window = Tk()
Window.title('BrickWall: First Line of Defense')
Window.configure(bg='Black')
Window.geometry('600x400')

a1 = StringVar("")

L1 = Label(Window, text='Secure Password Generator', font=20)
L1.place(x=210, y=50)

L2 = Label(Window, text='Length', width=7)
L2.place(x=150, y=150)

b1 = Entry(Window, bd=2)
b1.place(x=229, y=148)

L3 = Label(Window, text='Password')
L3.place(x=150, y=250)

Password_Output = Entry(Window, textvariable=a1, bd=2)
Password_Output.place(x=230, y=248)

# button to generate password, command references the function which gives the button its functionality
b = Button(Window, text="Generate Password")
b.configure(text='Generate', command=BrickWall)
b.place(x=270, y=300)

# stops window from from immediately opening and closing, keeps it open until the user closes the window themselves
Window.mainloop()