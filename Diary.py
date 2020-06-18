from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title('untitled-notepad')
    file=None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0,END)
        f=open(file, "r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile='untitled.txt',defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file== "":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"- notepad")
            print("file saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def schedule():
    pass
def calculator():
    global scvalue
    def click(event):
        global scvalue
        global screen
        text = event.widget.cget("text")
        print(text)
        if text == "=":
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                value = eval(screen.get())

            scvalue.set(value)
            screen.update()

        elif text == "C":
            scvalue.set("")
            screen.update()

        else:
            scvalue.set(scvalue.get() + text)
            screen.update()


    roo = Tk()
    roo.geometry("644x600")
    roo.title('calculator')

    scvalue = StringVar()
    scvalue.set("")
    screen = Entry(roo, textvar=scvalue, font='lucida 40 bold')
    screen.pack(fill=X, ipadx=8, padx=10, pady=10)

    f = Frame(roo, bg="grey")
    b = Button(f, text="9", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="8", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="7", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(roo, bg="grey")
    b = Button(f, text="6", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="5", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="4", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(roo, bg="grey")
    b = Button(f, text="3", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="2", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="1", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(roo, bg="grey")
    b = Button(f, text="0", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="+", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="*", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(roo, bg="grey")
    b = Button(f, text="=", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="/", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="C", padx=5, pady=2, font='lucida 35 bold')
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    roo.mainloop()
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo('title',"Notepad")

if __name__=='__main__':

    root=Tk()
    root.title("notepad")
    root.geometry('644x788')

    #add textarea
    TextArea=Text(root,font='lucida 13')
    file=None
    TextArea.pack(fill=BOTH,expand=True)


    #adding menubar
    MenuBar=Menu(root)

    #file menu starts
    FileMenu=Menu(MenuBar, tearoff=0)

    #to open new file
    FileMenu.add_command(label='New',command=newFile)

    #to openalready existing file
    FileMenu.add_command(label='Open',command=openFile)

    #to save current file
    FileMenu.add_command(label='Save',command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label='exit',command=quitApp)

    MenuBar.add_cascade(label='File',menu=FileMenu)
    #file menu ends

    #edit menu starts
    EditMenu=Menu(MenuBar,tearoff=0)

    #to give a feature of cut, copy, paste
    EditMenu.add_command(label='Cut',command=cut)
    EditMenu.add_command(label='Copy', command=copy)
    EditMenu.add_command(label='Paste', command=paste)
    MenuBar.add_cascade(label='Edit',menu=EditMenu)
    #edit menu ends

    #others menu starts
    OtherMenu=Menu(MenuBar,tearoff=0)

    #adding features of schedule and calculator
    OtherMenu.add_command(label='Schedule',command=schedule)
    OtherMenu.add_command(label='calculator',command=calculator)
    MenuBar.add_cascade(label='Others',menu=OtherMenu)
    #others menu ends

    #help menu starts
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label='About',command=about)
    MenuBar.add_cascade(label='Help',menu=HelpMenu)

    root.config(menu=MenuBar)

    #add scrollbar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview())
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()