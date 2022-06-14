import os
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Txt Documents", "*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Txt Documents", "*.*")])
        if file=="":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def aboutnotepad():
    tmsg.showinfo("About", "Notepad by Abhay Version 0.0.1")

if __name__ == "__main__":
    root = Tk()
    root.geometry("544x444")
    root.title("Notepad")

    # Text Area
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH, expand=True)

    # Let's Create a Menu Bar
    menubar = Menu(root)
    # File Menu Starts
    filemenu = Menu(menubar, tearoff=0)
    # To Open a New File
    filemenu.add_command(label="New", command=newfile)

    # To Open already existing File
    filemenu.add_command(label="Open File", command=openfile)

    # To Save the Current File
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitapp)
    menubar.add_cascade(label="File", menu=filemenu)
    # File Menu Ends

    # Edit Menu Starts
    EditMenu = Menu(menubar, tearoff=0)

    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=EditMenu)
    # Edit menu Ends

    # Help Menu Starts
    HelpMenu = Menu(menubar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=aboutnotepad)
    menubar.add_cascade(label="Help", menu=HelpMenu)
    # Help menu Ends
    root.config(menu=menubar)


    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)


    root.mainloop()