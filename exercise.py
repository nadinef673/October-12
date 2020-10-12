from tkinter import *


def build_gui():
    glass = Tk()
    glass.title("Adding Two Numbers")
    glass.geometry("450x400")
    glass.configure(background="purple")

    first_frame = Frame(glass)
    first_frame.pack()
    first_frame.configure(background="purple")

    second_frame = Frame(glass)
    second_frame.pack()
    second_frame.configure(background="purple")

    third_frame = Frame(glass)
    third_frame.pack()
    third_frame.configure(background="purple")

    fourth_frame = Frame(glass)
    fourth_frame.pack()
    fourth_frame.configure(background="purple")

    num_1 = IntVar()
    num_2 = IntVar()
    num_3 = IntVar()

    first_num_label = Label(first_frame, text="First Number", padx="21", pady="20")
    first_num_label.pack(side=LEFT)
    first_num_label.configure(background="purple")

    first_num_entry = Entry(first_frame, textvariable=num_1)
    first_num_entry.pack(side=RIGHT)

    second_num_label = Label(second_frame, text="Second Number", padx="10", pady="9")
    second_num_label.pack(side=LEFT)
    second_num_label.configure(background="purple")

    second_num_entry = Entry(second_frame, textvariable=num_2)
    second_num_entry.pack(side=RIGHT)

    third_num_label = Label(third_frame, text="The Result is:", padx="15", pady="15")
    third_num_label.pack(side=LEFT)
    third_num_label.configure(background="purple")
    third_num_entry = Entry(third_frame, textvariable=num_3)
    third_num_entry.pack(side=LEFT)

    def add_numbers():
        third_num_entry.insert(0, num_1.get() + num_2.get())

    add_btn = Button(text="Add", command=add_numbers)
    add_btn.pack(side=LEFT)

    def clear_all_num():
        first_num_entry.delete(0, END)
        second_num_entry.delete(0, END)
        third_num_entry.delete(0, END)

    clear_btn = Button(text="Clear", command=clear_all_num)
    clear_btn.pack(side=LEFT)

    def exit_program():
        glass.destroy()

    exit_btn = Button(text="Goodbye", command=exit_program)
    exit_btn.pack(side=LEFT)

    glass.mainloop()

build_gui()
