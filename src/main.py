#main.py

#See README for license information

#Main function for the EREBUS password vault
#Handles the GUI implementation and passes user input to the appropriate encryption File

#imports
from Tkinter import *
from ceasar import *
import tkMessageBox

#global variables to represent the current window
scrambler = False
saver = False
retriever = False

def ceasar():
  scramText = doCeasar(unscram.get(),shift.get())
  scram.set(scramText)

def doNothing():
    global scrambler
    if not scrambler:
        unscramframe = Frame(window)
        unscramframe.pack( side = TOP )
        shiftframe = Frame(window)
        shiftframe.pack()
        butframe = Frame(window)
        butframe.pack()
        botframe = Frame(window)
        botframe.pack( side = BOTTOM )
        
        unscramLabel = Label(unscramframe,text="Enter Unencrypted Password: ")
        unscramLabel.pack(side = LEFT) 
        global unscram
        unscram = StringVar()
        unscramEntry = Entry(unscramframe,bd = 5,textvariable = unscram)
        unscramEntry.pack(side = LEFT)
        shiftLabel = Label(shiftframe,text="Enter Shift Amount: ")
        shiftLabel.pack(side = LEFT)
        global shift
        shift = StringVar()
        shiftEntry = Entry(shiftframe,bd = 5,textvariable = shift)
        shiftEntry.pack(side = LEFT)
        
        scramButton = Button(butframe,text = "Encrypt!", command = ceasar)
        scramButton.pack()
        
        scramOutLabel = Label(botframe,text="Encrypted Password: ")
        scramOutLabel.pack(side=LEFT)
        global scram
        scram = StringVar()
        scramOut = Entry(botframe,bd = 5,textvariable = scram)
        scramOut.pack(side=LEFT)
        
        scrambler = True

if __name__ == '__main__':
    window = Tk()
    frame = Frame(window)
    frame.pack()
    #menubar
    bar = Menu(window)
    #scrambler menu option
    bar.add_command(label="Password Creator",command=doNothing)
    
    window.config(menu=bar)
    window.mainloop()