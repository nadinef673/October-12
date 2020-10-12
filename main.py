from tkinter import *

window = Tk()
window.configure(background="skyblue")
window.title("GUI LESSON")
window.geometry("750x700")


def add_function():
    a = int(en1.get())
    b = int(en2.get())
    result = a + b
    mytextbox.configure(text=result)
def clear_function():
    en1.delete(0, END)
    en2.delete(0, END)
    mytextbox.configure(text="result")


lbl1 = Label(window, text="First Number:", font="arial 10 bold")
lbl1.grid(row=0, column=0)
en1 = Entry(window)
en1.grid(row=0, column=1)
lb2 = Label(window, text="Second Number:", font="arial 10 bold")
lb2.grid(row=1, column=0)
en2 = Entry(window)
en2.grid(row=1, column=1)
lblresult = Label(window, text="Answer", font="arial 10 bold")
lblresult.grid(row=2, column=0)
mytextbox = Label(window, width=30)
mytextbox.grid(row=2, column=1)

my_button = Button(window, text="Add", command=add_function)
my_button.grid(row=3, column=2)
my_clearbutton = Button(window, text="clear", command=clear_function)
my_clearbutton.grid(row=3, column=5)

window.mainloop()