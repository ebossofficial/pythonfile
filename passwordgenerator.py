#written by ebossofficial
#using Tkinter GUI module
import os
import random
import string
from tkinter import *

def createPwd():
    try:
        length = int(e1.get())
    except ValueError:
        return
    chars = string.ascii_letters + string.digits + '@!#'
    random.seed = (os.urandom(1024))
    e2.config(state=NORMAL)
    e2.delete(0,'end')
    e2.insert(0,''.join(random.choice(chars) for i in range(length)))
    e2.config(state="readonly")

mainWindow = Tk()
mainWindow.title('CODELAGOS Password Generator Application')

mainWindow.resizable(1,1)

f0 = Frame(mainWindow)

f0.pack(side=TOP,pady=8,padx=7,fill=X,expand=4)

Label(f0,text="Enter desired Length: ",anchor=E).grid(row=0,column=0,sticky=E)

e1 = Entry(f0)
e1.insert(0,'')
e1.grid(row=0,column=1)

btn = Button(f0,text="Generate")
btn['command'] = lambda: createPwd()
btn.grid(row=0,column=2,rowspan=1,padx=10,ipadx=10)

Label(f0,text="Generated password: ",anchor=E).grid(row=1,column=0,sticky=E)
e2 = Entry(f0)
e2.grid(row=1,column=1)

createPwd()

#starting main window
mainWindow.mainloop()