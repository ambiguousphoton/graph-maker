from tkinter import font
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter.font as font

root = Tk()

root.title("GRAPH MAKER")

f = font.Font(weight='bold', size = 16)

f2= font.Font(weight='bold',size = 35)

lb2 = Label(root, text =" graph maker",font=f,fg='black').grid(row = 0, column = 0,pady = 7)

lbl = Label(root, text =" AI developed by Vyoam ",font=f,fg='red').grid(row = 1, column = 0,pady = 7)

inputbox = Entry(root, width=59, fg='red')

inputbox.grid(row = 2, column = 0,pady = 7,padx=5)

def click():
    string = inputbox.get()
    string = string.lower()

    x = np.arange(0,4*np.pi,0.1)
    if "graph" in string:

        if "sin graph" in string:
            y = np.sin(x)
        
        if "cos graph" in string:
            y = np.cos(x)

        if "tan graph" in string:
            y = np.tan(x)

        if "cosec graph" in string:
            y = 1/np.sin(x)

        if "sec graph" in string:
            y = 1/np.cos(x)

        if "cot graph" in string:
            y = 1/np.tan(x)

        plt.plot(x,y)
        plt.show()



btn = Button(root, text= "PRESS",borderwidth=1, padx=2, pady=2 , bg ='grey', fg='white',font=f,command = click).grid(row = 2, column = 1,pady = 7, padx= 7)

mainloop()

        
