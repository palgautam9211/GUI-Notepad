from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def fileMenu():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All files","*.*"),("Text Documents" ,"*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        f=open(file,"r")
        TextArea.insert(1.0,file)
        f.close()
def saveFile():
    global file
    if file==None:
       file=asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                           filetypes=[("All files","*.*"),("Text Documents" ,"*.txt")])
       if file=="":
           file=None
       else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
    else:
      f = open(file, "w")
      f.write(TextArea.get(1.0, END))
      f.close()


def exit():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def aboutNotepad():
    showinfo("Notepad","Designed by Gautam Pal")
def aboutFounder():
    showinfo("Abhi nahi bhai baad me")

root=Tk()
root.title(" Gautam's Notepad")

#text area
TextArea=Text(root,font="bold,13")
TextArea.pack(expand=True,fill=BOTH)

#create a menu bar
menuBar=Menu(root)

#file menu starts here
fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New" ,command=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Exit",command=exit)

menuBar.add_cascade(label="File",menu=fileMenu)


#edit menu starts
editMenu=Menu(menuBar,tearoff=0)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

menuBar.add_cascade(label="Edit",menu=editMenu)

#help menu starts
helpMenu=Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About Notepad",command=aboutNotepad)
helpMenu.add_command(label="About Gautam",command=aboutFounder)
menuBar.add_cascade(label="Help",menu=helpMenu)

#for displaying the menu bar
root.config(menu=menuBar)

#to show the scroll bar
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)


root.mainloop()