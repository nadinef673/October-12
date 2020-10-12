from tkinter import *
import tkinter

def input():
    entry1.delete(0, END)
    return None

def add_numbers():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    answer = num1 + num2
    result_label.configure(text=answer)
def clear():
    num1_entry.delete(0, END)
    num2_entry.delete(0, END)
    result_label.configure(text=answer)

glass = Tk()
glass.title("Addition")
glass.geometry("500x500")
glass.configure(background="purple")

label1 = Label(glass, text="First Number")
label1.grid(row=0, column=0)

num1_entry = Entry(glass, width=20, relief="solid")
num1_entry.grid(row=0, column=1)

label2 = Label(glass, text="Second Number", relief="solid")
label2.grid(row=0, column=2)

num2_entry = Entry(glass)
num2_entry.grid(row=1, column=1)
result_label = Label(glass, text="Result")
result_label.grid(row=2, column=0)
calculate_button = Button(glass, text="Add", command="add_numbers")
calculate_button.grid(row=3, column=0, columnspan=2)
calculate_button = Button(glass, text="Clear", command="clear")
calculate_button.grid(row=3, column=8)

glass.mainloop()