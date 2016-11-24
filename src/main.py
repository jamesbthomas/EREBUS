#main.py

#See README for license information

#Main function for the EREBUS password vault
#Handles the GUI implementation and passes user input to the appropriate encryption File

#imports
from tkinter import *
import ceasar

#global variables to represent the current window
scrambler = False
saver = False
retriever = False

def doNothing():
    global scrambler
    if not scrambler:
        scramblerLabel = Label(window,text="Enter Unencrypted Password: ")
        scramblerLabel.pack(side = LEFT)
        
        unscramEntry = Entry(window,bd = 5)
        unscramEntry.pack(side=RIGHT)
        #text = Text(window)
        #text.insert(INSERT,"Hello World!")
        #text.pack()
        scrambler = True

if __name__ == '__main__':
    window = Tk()
    #menubar
    bar = Menu(window)
    #scrambler menu option
    bar.add_command(label="Password Creator",command=doNothing)
    
    window.config(menu=bar)
    window.mainloop()