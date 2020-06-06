import tkinter as tk

window = tk.Tk()
window.title("Paint")
canvas = tk.Canvas(width=500, height=500)
canvas.pack()

def paint(event):
    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
    canvas.create_line( x1, y1, x2, y2, fill='#000000' )

canvas.bind("<B1-Motion>", paint)
window.bind("<Escape>", lambda e: window.destroy())
window.mainloop()
