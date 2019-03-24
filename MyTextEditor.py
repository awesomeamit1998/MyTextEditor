from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox
import tkinter.scrolledtext as ScrolledText
from tkinter import *
from PIL import ImageTk
#root is the root window into which all other widgets go. It is an instance of the class Tk, and every tkinter application must have exactly one instance of this class. app is an instance of the class App, which is a subclass of Frame.
root=Tk(className=" AJ Text Editor")
textArea=ScrolledText.ScrolledText(root,width=100,height=80,bg='green')
#
#FUNCTIONS
#
def openFile():
	file=filedialog.askopenfile(parent=root,mode='rb',title='select a text file')
	if file!=None:
		contents=file.read()
		textArea.insert('1.0',contents)
		file.close()
def saveFile():
	file=filedialog.asksaveasfile(mode='w')
	if file!=None:
		#Slice of the last character from get,as an extra enter is added
		data=textArea.get('1.0',END+'-1c')
		file.write(data)
		file.close()
def quit():
	if messagebox.askyesno("Quit","Are u sure u want to quit"):
		root.destroy()
def about():
	label=messagebox.showinfo("A python Text editor using tkinter!")
#Menu options
menu=Menu(root)
root.configure(background = 'black')
root.config(menu=menu)
fileMenu=Menu(menu)
#Creates a new hierarchical menu by associating a given menu to a parent menu(add_cascade)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Print")
helpMenu=Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About", command=about)
#fileMenu.add_seperator()
fileMenu.add_command(label="Exit",command=quit)
textArea.pack()
photo = PhotoImage(file = "aa.png")
w = Label(root, image=photo)
w.pack()
root.mainloop()
