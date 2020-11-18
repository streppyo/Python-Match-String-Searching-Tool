import os
import sys
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory

import pyperclip

# TODO: Improve UI in fetching results (scrollbar, padding)

sys.tracebacklimit = -1


path = ""

result = []
resultcp = ""

window = Tk()


window.title("File String Searcher")
#window.geometry("340x300")
window.resizable(0,0)
lbl1 = Label(window, text="Please enter the string to find below")
lbl1.grid(column=0, row=0, sticky=W, padx=(10,0))

path_var = tk.StringVar()
ext_var = tk.StringVar()
str_var = tk.StringVar()
warn_var = tk.StringVar()

ent1 = Entry(window, width=35, textvariable= path_var,state='disabled')
ent1.grid(column=0, row=1)



def askdir():
    path = askdirectory(title='Select directory to search')
    path_var.set(path)

btn = Button(window, text="Browse", command = askdir)
btn.grid(column=1, row=1,padx=(10,20))


lbl2 = Label(window, text="Please enter the file extension to search\n(Leave empty to search through all files)")
lbl2.grid(column=0, row=2, sticky=W, padx=(10,0))

ent2 = Entry(window, width=35, textvariable= ext_var)
ent2.grid(column=0, row=3)

lbl3 = Label(window, text="Please enter the string to find below")
lbl3.grid(column=0, row=4, sticky=W, padx=(10,0))

ent3 = Entry(window, width=35, textvariable= str_var)
ent3.grid(column=0, row=5)

lbl4 = Label(window, textvariable = warn_var, fg = "#c42b00")
lbl4.grid(column=0, row=6, sticky=W, padx=(10,0))

def mainrun():

    result = []  # Initialise reults
    resultcp = ""

    path = path_var.get()

    if len(path) == 0:
        #Message ("Please specify path to search.")
        warn_var.set("Please specify path to search.")
        print("no")
        return

    nam = str_var.get()


    if len(nam) == 0:
        #Message ("Please specify the string to search.")
        warn_var.set("Please specify the string to search.")
        print("no")
        return

    ext = ext_var.get()


    warn_var.set("")

#    print("Searching for matching content through files ending with " + ext + " for string "  + nam + "...")

    for  root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name.endswith(ext):
                str = ""
                try:
                    f = open(os.path.join(root, name), "r")
                    str = f.read()
                except:
                    pass
                try:
                    f = open(os.path.join(root, name), "r","utf-8")
                    str = f.read()
                except:
                    pass
                try:
                    f = open(os.path.join(root, name), "r","utf-16")
                    str = f.read()
                except:
                    pass
                try:
                    f = open(os.path.join(root, name), "r","unicode")
                    str = f.read()
                except:
                    pass
                if nam in str:
#                    print(os.path.join(root, name))
                    result.append(os.path.join(root, name))
                    resultcp = resultcp + os.path.join(root, name) + "\n"

    print(result)

    res = Toplevel(window)
    var = StringVar()
    var.set(result)

    lb = Listbox(res, listvariable=var, width=50, height=20, selectmode='extended')

    txt1 = Label(res, text="The string exists in the following files:")
    txt1.pack(side="top",expand=False)
    lb.pack(side="left",fill="both", expand=True)

    def cp():
        pyperclip.copy(resultcp)

    CP = Button(res, text = "Copy to\n   Clipboard   ", command = cp)
    CP.pack(side="right", expand=False)

#    print(result)


B = Button(window, text = "\n      Go      \n", command = mainrun)
B.grid(column=0, row=7, padx=(10, 10), pady=(10, 10), sticky = W)

def clear():

    warn_var.set("")

    str_var.set("")

    ext_var.set("")

    path_var.set("")


C = Button(window, text = "\n    Clear    \n", command = clear)
C.grid(column=0, row=7, padx=(10, 10), pady=(10, 10), sticky = E)

window.mainloop()
print(path)
