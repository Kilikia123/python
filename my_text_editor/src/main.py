import textEditor

root = textEditor.Tk()
text = textEditor.Text(root, width=10000, height=10000)
text.pack()
root.geometry('1000x700')
My_txt_edt = textEditor.Node(root)
root.mainloop()
