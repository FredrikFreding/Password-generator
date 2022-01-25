from tkinter import *

# Creating the window.
root = Tk()
root.title("Password Generator")
root.geometry("300x300")

#  DoubleVar: Holds a float; default value 0.0
v1 = DoubleVar()

def createPassword():
    pass

# Creating Label Widgets with text.
header = Label(root, text="Password Generator")
sliderText = Label(root, text="How long do you want your password to be?")
btn = Button(root, text='Create Password', command=createPassword)
emptyLine = Label(root, text=" ")

# Creating a Label Widget with a slider (scale).
slider = Scale( root, variable = v1, 
           from_ = 5, to = 30, 
           orient = HORIZONTAL)

# Changing configs of widgets.
header.config(font=(30))

# Packing everything so it shows on our screen.
header.pack(anchor = CENTER)
emptyLine.pack()
sliderText.pack()
slider.pack(anchor = CENTER)
btn.pack(side=BOTTOM)
emptyLine.pack()

# Creating the loop that runs until we close the window.
root.mainloop()