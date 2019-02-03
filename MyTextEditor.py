from tkinter import *
import tkinter.scrolledtext as ScrolledText
root=Tk(className="Text Editor")
textArea=ScrolledText.ScrolledText(root,width=100,height=80)
#Menu options
menu=Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Print")

helpMenu=Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About")
#fileMenu.add_seperator()
fileMenu.add_command(label="Exit")
textArea.pack()

#Keep the window open
root.mainloop()
