import time
import tkinter as tk

w = tk.Tk()
c = tk.Label()
c.pack()

def t():
    s = time.strftime("%H:%M:%S")
    c.config(text=s)
    c.after(1000, t)

t()
w.mainloop()
