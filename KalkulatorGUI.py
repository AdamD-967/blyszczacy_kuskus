import tkinter as tk

w = tk.Tk()

ex = tk.Entry()
ex.grid(row=0, column=0, columnspan=2)
out = tk.Entry()
out.grid(row=0, column=2)

def cr(): ex.insert(tk.END, "**")
def cnc(): ex.insert(tk.END, ")")
def cno(): ex.insert(tk.END, "(")
def cd(): ex.insert(tk.END, "/")
def ct(): ex.insert(tk.END, "*")
def c1(): ex.insert(tk.END, '1')
def c2(): ex.insert(tk.END, '2')
def c3(): ex.insert(tk.END, '3')
def c4(): ex.insert(tk.END, '4')
def c5(): ex.insert(tk.END, '5')
def c6(): ex.insert(tk.END, '6')
def c7(): ex.insert(tk.END, '7')
def c8(): ex.insert(tk.END, '8')
def c9(): ex.insert(tk.END, '9')
def c0(): ex.insert(tk.END, '0')
def cp(): ex.insert(tk.END, '+')
def cm(): ex.insert(tk.END, '-')
def go(event): out.insert(tk.END, str(eval(ex.get())))
def cl():
    out.delete(0, tk.END)
    ex.delete(0, tk.END)

b1 = tk.Button(text="1", command=c1)
b1.grid(row=1, column=0)
b2 = tk.Button(text="2", command=c2)
b2.grid(row=1, column=1)
b3 = tk.Button(text="3", command=c3)
b3.grid(row=1, column=2)
b4 = tk.Button(text="4", command=c4)
b4.grid(row=2, column=0)
b5 = tk.Button(text="5", command=c5)
b5.grid(row=2, column=1)
b6 = tk.Button(text="6", command=c6)
b6.grid(row=2, column=2)
b7 = tk.Button(text="7", command=c7)
b7.grid(row=3, column=0)
b8 = tk.Button(text="8", command=c8)
b8.grid(row=3, column=1)
b9 = tk.Button(text="9", command=c9)
b9.grid(row=3, column=2)
b0 = tk.Button(text="0", command=c0)
b0.grid(row=1, column=3)

bp = tk.Button(text="+", command=cp)
bp.grid(row=2, column=3)
bm = tk.Button(text="-", command=cm)
bm.grid(row=3, column=3)
bc = tk.Button(text="cl", command=cl)
bc.grid(row=4, column=0)
bt = tk.Button(text="*", command=ct)
bt.grid(row=4, column=1)
bd = tk.Button(text="/", command=cd)
bd.grid(row=4, column=2)
bno = tk.Button(text="(", command=cno)
bno.grid(row=5, column=0)
bnc = tk.Button(text=")", command=cnc)
bnc.grid(row=5, column=1)
br = tk.Button(text="^", command=cr)
br.grid(row=4, column=3)

w.bind("<Return>", go)

w.mainloop()
