from tkinter import *
import pyperclip
import string
import random

# Creating the window.
root = Tk()
root.title("Password Generator")
root.geometry("300x300")

#  DoubleVar: Holds a float; default value 0.0
v1 = DoubleVar()

# Create a password and write it to the screen, this function start when createPWD button is clicked.
def createPassword():
    charsLen = slider.get()

    chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(chars)

    global pwd
    pwd = []
    
    for i in range(charsLen):
        pwd.append(random.choice(chars))
    
    random.shuffle(pwd)
    pwd = "".join(pwd)
    pwdText.config(text=pwd)

# Copy the password to clipboard. This function starts when copyPWD button is clicked.
def copyPassword():
    pyperclip.copy(pwd)

# Creating Label Widgets with text.
header = Label(root, text="Password Generator")
sliderText = Label(root, text="How long do you want your password to be?")
createPWD = Button(root, text='Create Password', command=createPassword)
copyPWD = Button(root, text='Copy to clipboard', command=copyPassword)
pwdText = Label(root, text="Your new password")
emptyLine = Label(root, text=" ")

# Creating a Label Widget with a slider (scale).
slider = Scale( root, variable = v1, 
           from_ = 5, to = 30, 
           orient = HORIZONTAL)

# Changing configs of widgets.
header.config(font=(30))

# Packing everything so it shows on our screen.
header.pack(anchor = CENTER)
sliderText.pack()
slider.pack(anchor = CENTER)
copyPWD.pack()
pwdText.pack()
createPWD.pack(side=BOTTOM)

# Creating the loop that runs until we close the window.
root.mainloop()