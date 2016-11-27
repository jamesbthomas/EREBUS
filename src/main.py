#main.py

#See README for license information

#Main function for the EREBUS password vault
#Handles the GUI implementation and passes user input to the appropriate encryption File

#imports
from Tkinter import *
import tkFont
from ceasar import *
import tkMessageBox

def ceasar():
  if shift.get():
    scramText = doCeasar(unscram.get(),shift.get())
    scram.set(scramText)

def ceasarMenu():
    global ceasar
    if not ceasar:
        unscramframe = Frame(window)
        unscramframe.pack( side = TOP )
        shiftframe = Frame(window)
        shiftframe.pack()
        butframe = Frame(window)
        butframe.pack()
        botframe = Frame(window)
        botframe.pack()
        
        unscramLabel = Label(unscramframe,text="Enter Phrase: ")
        unscramLabel.pack(side = LEFT) 
        global unscram
        unscram = StringVar()
        unscramEntry = Entry(unscramframe,bd = 5,textvariable = unscram)
        unscramEntry.pack(side = LEFT)
        shiftLabel = Label(shiftframe,text="Enter Shift: ")
        shiftLabel.pack(side = LEFT)
        global shift
        shift = StringVar()
        shiftEntry = Entry(shiftframe,bd = 5,textvariable = shift)
        shiftEntry.pack(side = LEFT)
        
        scramButton = Button(butframe,text = "Encrypt!", command = ceasar)
        scramButton.pack()
        
        scramOutLabel = Label(botframe,text="Password: ")
        scramOutLabel.pack(side=LEFT)
        global scram
        scram = StringVar()
        scramOut = Entry(botframe,bd = 5,textvariable = scram)
        scramOut.pack(side=LEFT)
        
        ceasar = True

def doHome():
    global home
    if not home:
        homeFrame = Frame(window)
        homeFrame.pack()
        
        titleLabel = Label(homeFrame,text="EREBUS",font=titleFont)
        titleLabel.pack()
        
        subtitleLabel = Label(homeFrame,text="The Home Password Vault",font=subTitleFont)
        subtitleLabel.pack()
    
        home = True

if __name__ == '__main__':
    #make some variables
    ceasar = False
    home = False
    #root window
    window = Tk()
    window.minsize(width=250,height=150)
    #make some fonts
    titleFont = tkFont.Font(family="Arial Black",size=20)
    subTitleFont = tkFont.Font(family="Helvetica",size=12)
    doHome()
    #menubar
    bar = Menu(window)
    #home menu
    bar.add_command(label="Home",command=doHome)
    #scrambler menu option
    scrambler = Menu(bar,tearoff=0)
    scrambler.add_command(label="Caesar",command=ceasarMenu)
    bar.add_cascade(label="Creator",menu=scrambler)
    #saver menu option
    bar.add_command(label="Saver")
    #retriever menu option
    bar.add_command(label="Retriever")
    window.config(menu=bar)
    window.mainloop()