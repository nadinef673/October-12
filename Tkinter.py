from tkinter import *
import tkinter

def testing():
    mytext = "Hello guys. How are you?"
    theLabel_txtbx.insert(0, mytext)
    return None

glass = Tk()
glass.title("GUI APP")
glass.geometry("500x500")
glass.configure(background="purple")
theLabel = Label(glass, text="Greetings to you all", background="purple")
theLabel.pack()
theLabel_txtbx=Entry(glass, width=30)
theLabel_txtbx.pack()
my_button = Button(glass, text="Click me", bg="blue", command=testing)
my_button.pack()









glass.mainloop()

