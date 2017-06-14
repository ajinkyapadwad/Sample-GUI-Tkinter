"""
AJINKYA June 2017
"""

from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
import PIL 
# from PIL import ImageTk,Image


class Example(Frame):

    def __init__(self, parent):
        # bg = Image.open("bg.jpg")
        # background_image=ImageTk.PhotoImage(bg)
        # background_label = Label(parent, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        

        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("User Setup")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.centreWindow()
        self.pack(fill=BOTH, expand=1)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.quit)
        # menubar.add_cascade(label="File", menu=fileMenu)

        firstNameLabel = Label(self, text="Username")
        firstNameLabel.grid(row=0, column=0, sticky=W+E)
        lastNameLabel = Label(self, text="Password")
        lastNameLabel.grid(row=1, column=0, sticky=W+E)
        countryLabel = Label(self, text="Country")
        countryLabel.grid(row=2, column=0, sticky=W+E)
        addressLabel = Label(self, text="Address")
        addressLabel.grid(row=3, column=0, pady=10, sticky=W+E+N)
        
        firstNameText = Entry(self, width=20)
        firstNameText.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        lastNameText = Entry(self, width=20)
        lastNameText.grid(row=1, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        
        self.countryVar = StringVar()
        self.countryCombo = ttk.Combobox(self, textvariable=self.countryVar)
        self.countryCombo['values'] = ('United States', 'United Kingdom', 'France')
        self.countryCombo.current(1)
        self.countryCombo.bind("<<ComboboxSelected>>", self.newCountry)
        self.countryCombo.grid(row=2, column=1, padx=5, pady=5, ipady=2, sticky=W)
        
        addressText = Text(self, padx=5, pady=5, width=20, height=6)
        addressText.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        
        
        self.titleVar = StringVar()
        self.titleVar.set("[User Status]")
        Label(self, textvariable=self.titleVar).grid(
            row=4, column=1, sticky=W+E
        )   # a reference to the label is not retained
        
        title = ['Admin', 'End-user', 'Programmer']
        titleList = Listbox(self, height=5)
        for t in title:
            titleList.insert(END, t)
        titleList.grid(row=3, column=2, columnspan=2, pady=5, sticky=N+E+S+W)
        titleList.bind("<<ListboxSelect>>", self.newTitle)
        
        okBtn = Button(self, text="OK", width=10, command=self.onConfirm)
        okBtn.grid(row=4, column=2, padx=5, pady=3, sticky=W+E)
        closeBtn = Button(self, text="Close", width=10, command=self.onExit)
        closeBtn.grid(row=4, column=3, padx=5, pady=3, sticky=W+E)
    
    def centreWindow(self):
        w = 450
        h = 295
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onExit(self):
        self.quit()
    
    def newCountry(self, event):
        print(self.countryVar.get())
    
    def fullChecked(self):
        if self.fullTimeVar.get() == 1:
            self.parent.title("Simple Window (full-time)")
        else:
            self.parent.title("Simple Window")
    
    def newTitle(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        self.titleVar.set(value)
    
    def onConfirm(self):
        box.showinfo("Information", "Thank you!")

def main():
    root = Tk()

    root.resizable(width=TRUE, height=TRUE)
    # resizable

    app = Example(root)

    # img = ImageTk.PhotoImage(Image.open("logo.jpg"))
    # panel = Label(root, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "no")

    root.mainloop()

if __name__ == '__main__':
    main()
