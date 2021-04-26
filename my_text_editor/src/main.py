import text_editor

root = text_editor.Tk()
text = text_editor.Text(root, width=10000, height=10000)
text.pack()
root.geometry('1000x700')
My_txt_edt = text_editor.Node(root)
root.mainloop()
