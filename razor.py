from cgitb import text
from cmath import exp
from fileinput import close
from tkinter import *
import tkinter.ttk as ttk
from datetime import datetime
from tkinter  import messagebox
from tkinter import filedialog,simpledialog
import tkinter
from tkinter.scrolledtext import ScrolledText
from turtle import title
# from turtle import bgcolor
import pyglet

# Fonts:
pyglet.font.add_file('fonts/FiraCode-Retina.ttf')

# Colors:
mainColor = "#373737"
secondColor = "#272727"
textColor = "#fff"

# Root widget:
root = Tk()
root.title('Razor Pad')
root.resizable(True, True)
root.overrideredirect(True) # Hides tkinter default titlebar
style = tkinter.ttk.Style(root)
root.tk.call('source', 'themes/azure dark/azure dark.tcl')
style.theme_use('azure')

def moveApp(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

def quitter(e):
    root.quit()

# Create custom title bar:d
titleBar = Frame(root, bg=secondColor, relief="raised")
titleBar.pack(expand=1, fill=X, padx=8, pady=4)
titleBar.bind("<B1-Motion>", moveApp)

mainIco = PhotoImage(file="img/icons8-knife-64.png")
mainIcoLbl = Label(titleBar, image=mainIco, bg=secondColor, height=12)
mainIcoLbl.pack(side=LEFT)

closeIco = PhotoImage(file="img/icons8-w-close-24.png")
closeBtn = Button(titleBar, image=closeIco, bg=secondColor, width=12, height=12, bd=0)
closeBtn.pack(side=RIGHT, pady=4, padx=4)
closeBtn.bind("<Button-1>", quitter)

collapseIco = PhotoImage(file="img/icons8-w-fullscreen-24.png")
collapseBtn = Button(titleBar, image=collapseIco, bg=secondColor, width=17, height=17, bd=0)
collapseBtn.pack(side=RIGHT, pady=4, padx=10)
# collapseBtn.bind("<Button-1>", quitter)

hideIco = PhotoImage(file="img/icons8-w-minus-24.png")
hideBtn = Button(titleBar, image=hideIco, bg=secondColor, width=12, height=12, bd=0)
hideBtn.pack(side=RIGHT, pady=4, padx=10)
# hideBtn.bind("<Button-1>", quitter)

# Scrollable notepad window
notepad = ScrolledText(root, width=90, height=40, font=("FiraCode-Retina", 12))
notepad.vbar.config(troughcolor=mainColor, bg="blue")
fileName = ''

# Keyboard commands:
def cmdNew(e):
    print('new')
    global fileName
    if len(notepad.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("RazorPad", "Do you want to save changes?"):
            cmdSave()
        else:
            notepad.delete(0.0, END)
    root.title("RazorPad")
root.bind("<Control-n>", cmdNew)

def cmdOpen(e):
    fd = filedialog.askopenfile(parent = root, mode = 'r')
    t = fd.read()     # t is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)
root.bind("<Control-o>", cmdOpen)

def cmdSave(e):
    fd = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    if fd != None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")
root.bind("<Control-s>", cmdSave)

def cmdSaveAs(e):
    fd = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
    t = notepad.get(0.0, END)     #t stands for the text taken from notepad
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")
root.bind("<Control-Shift-S>", cmdSaveAs)

def cmdExit(e):
    if messagebox.askyesno("RazorPad", "Are you sure you want to exit?"):
        root.destroy()
root.bind("<Control-q>", cmdExit)
       
def cmdFind(e):
    notepad.tag_remove("Found",'1.0', END)
    find = simpledialog.askstring("Find", "Search String:")
    if find:
        idx = '1.0'
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground=textColor, background="#0059E6555")
    notepad.bind("<1>", click)
root.bind("<Control-f>", cmdFind)

def click(event):     # Handling click event
    notepad.tag_config('Found',background='white',foreground='black')

def cmdTimeDate():     # Edit menu Time/Date option
    now = datetime.now()
    dtString = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
    label = messagebox.showinfo("Time/Date", dtString)

# Darkmode
#isDarkMode = False
def toggle_darkmode():
    root.config(bg=secondColor)
    notepad.config(bg=mainColor, fg=textColor)


toggle_darkmode()

notepad.pack()
root.mainloop()
