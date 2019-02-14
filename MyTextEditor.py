from tkinter import Tk,scrolledtext,Menu,filedialog
import tkinter.scrolledtext as ScrolledText
root=Tk(className="Text Editor")
textArea=ScrolledText.ScrolledText(root,width=100,height=80)
#
#FUNCTIONS
#
def openFile():
	file=filedialog.askopenfile(parent=root,mode='rb',title='select a text file')
	if file!=None:
		contents=file.read()
		textArea.insert('1.0',contents)
		file.close()
#Menu options
menu=Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open",command=openFile)
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
