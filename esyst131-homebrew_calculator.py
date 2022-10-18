
'''

ESYST-131 - Homebrew Calculator

A. Suresh Kumar (5/28/22)

==================================

This program will create a GUI window

with a mockup of a calculator's layout.

==================================

Variables:

window     # variable to hold created tkinter GUI window

==================================

Functions:

none

==================================

Imports:

tkinter      # used to create GUI for python program

'''

import tkinter

window = tkinter.Tk()

#create top label with name
tkinter.Label(window, text="Arjun Suresh Kumar - Calculator", justify="center").grid(row=1, column=1, columnspan=4)

#create buttons for all numbers
tkinter.Button(window, text="9").grid(row=2, column=3, sticky="nesw")
tkinter.Button(window, text="8").grid(row=2, column=2, sticky="nesw")
tkinter.Button(window, text="7").grid(row=2, column=1, sticky="nesw")
tkinter.Button(window, text="6").grid(row=3, column=3, sticky="nesw")
tkinter.Button(window, text="5").grid(row=3, column=2, sticky="nesw")
tkinter.Button(window, text="4").grid(row=3, column=1, sticky="nesw")
tkinter.Button(window, text="3").grid(row=4, column=3, sticky="nesw")
tkinter.Button(window, text="2").grid(row=4, column=2, sticky="nesw")
tkinter.Button(window, text="1").grid(row=4, column=1, sticky="nesw")
tkinter.Button(window, text="0").grid(row=5, column=2, sticky="nesw")

#create operator buttons
tkinter.Button(window, text="x").grid(row=2, column=4, sticky="nesw")
tkinter.Button(window, text="/").grid(row=3, column=4, sticky="nesw")
tkinter.Button(window, text="-").grid(row=4, column=4, sticky="nesw")
tkinter.Button(window, text="+").grid(row=5, column=4, sticky="nesw")

#create "=" button
tkinter.Button(window, text="=").grid(row=5, column=3, sticky="nesw")

window.mainloop()