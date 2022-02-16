import re
from tkinter import *
import tkinter
from tkinter.ttk import *
from datetime import datetime
from tkinter  import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
import pyglet, os

pyglet.font.add_file('fonts/FiraCode-Retina.ttf')

# Darkmode:
# def darkTheme(root):
#     style = tkinter.ttk.Style(root)
#     root.tk.call('source', 'themes/azure dark/azure dark.tcl')
#     style.theme_use('azure')
#     style.configure('Accentbutton', foreground='white')
#     style.configure('Togglebutton', foreground='white')
#     return style

# Root widget:
root = Tk()
root.title('Razor Pad')
root.resizable(True, True)
# style = darkTheme(root)

# Scrollable notepad window
notepad = ScrolledText(root, width = 90, height = 40, font="FiraCode-Retina")
fileName = ''

# Functions for commands:
def cmdNew():     # File menu New option
    global fileName
    if len(notepad.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("Notepad", "Do you want to save changes?"):
            cmdSave()
        else:
            notepad.delete(0.0, END)
    root.title("Notepad")

def cmdOpen():     # File menu Open option
    fd = filedialog.askopenfile(parent = root, mode = 'r')
    t = fd.read()     # t is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)
    
def cmdSave():     # File menu Save option
    fd = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    if fd != None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")
     
def cmdSaveAs():     # File menu Save As option
    fd = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
    t = notepad.get(0.0, END)     #t stands for the text gotten from notepad
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")

def cmdExit():     # File menu Exit option
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()

def cmdCut():     # Edit menu Cut option
    notepad.event_generate("<<Cut>>")

def cmdCopy():     # Edit menu Copy option
    notepad.event_generate("<<Copy>>")

def cmdPaste():     # Edit menu Paste option
    notepad.event_generate("<<Paste>>")

def cmdClear():     # Edit menu Clear option
    notepad.event_generate("<<Clear>>")
       
def cmdFind():     # Edit menu Find option
    notepad.tag_remove("Found",'1.0', END)
    find = simpledialog.askstring("Find", "Find what:")
    if find:
        idx = '1.0'
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground = 'white', background = 'blue')
    notepad.bind("<1>", click)

def click(event):     # Handling click event
    notepad.tag_config('Found',background='white',foreground='black')

def cmdSelectAll():     # Edit menu Select All option
    notepad.event_generate("<<SelectAll>>")
    
def cmdTimeDate():     # Edit menu Time/Date option
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Time/Date", dtString)

# Notepad menu items:
notepadMenu = Menu(root)
root.configure(menu=notepadMenu)

# File menu:
fileMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='File', menu = fileMenu)

# Adding options in file menu:
fileMenu.add_command(label='New', command = cmdNew)
fileMenu.add_command(label='Open...', command = cmdOpen)
fileMenu.add_command(label='Save', command = cmdSave)
fileMenu.add_command(label='Save As...', command = cmdSaveAs)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command = cmdExit)

# Edit menu:
editMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Edit', menu = editMenu)

# Edit menu options
editMenu.add_command(label='Cut', command = cmdCut)
editMenu.add_command(label='Copy', command = cmdCopy)
editMenu.add_command(label='Paste', command = cmdPaste)
editMenu.add_command(label='Delete', command = cmdClear)
editMenu.add_separator()
editMenu.add_command(label='Find...', command = cmdFind)
editMenu.add_separator()
editMenu.add_command(label='Select All', command = cmdSelectAll)
editMenu.add_command(label='Time/Date', command = cmdTimeDate)

# Darkmode
#isDarkMode = False
def toggle_darkmode():
    # isDarkMode = not isDarkMode
    mainColor = "#373737"
    secondColor = "#272727"
    textColor = "#fff"
    root.config(bg=secondColor)
    notepadMenu.config(bg=secondColor, fg=textColor)
    editMenu.config(bg=mainColor, fg=textColor)
    fileMenu.config(bg=mainColor, fg=textColor)
    notepad.config(bg=mainColor, fg=textColor)

toggle_darkmode()

notepad.pack()
root.mainloop()
