import tkinter
from tkinter import *
from CodeWarrior import text
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

FILE_NAME = "Default"

class Node(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("Arman's Node")
        self.pack(fill=BOTH, expand=1)
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        File = Menu(menubar)
        File.add_command(label='New', command=self.new_file)
        File.add_command(label='Open', command=self.open_file)
        File.add_command(label='Save', command=self.save_file)
        File.add_command(label='Save as', command=self.save_as)
        File.add_separator()
        File.add_command(label='Exit', command=self.my_exit)
        menubar.add_cascade(label='File', menu=File)

    def new_file(self):
        global FILE_NAME
        FILE_NAME = "Untitled"
        text.delete('1.0', tkinter.END)

    def save_file(self):
        data = text.get('1.0', tkinter.END)
        out = open(FILE_NAME, 'w')
        out.write(data)
        out.close()

    def save_as(self):
        out = asksaveasfile(mode='w', defaultextension='txt')
        data = text.get('1.0', tkinter.END)
        try:
            out.write(data.rstrip())
        except Exception:
            showerror(title="Error", message="Saving file error")

    def open_file(self):
        global FILE_NAME
        inp = askopenfile(mode="r")
        if inp is None:
            return
        FILE_NAME = inp.name
        data = inp.read()
        text.delete('1.0', tkinter.END)
        text.insert('1.0', data)

    def my_exit(self):
        exit()