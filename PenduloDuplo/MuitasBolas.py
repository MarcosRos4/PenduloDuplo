import tkinter as tk
from random import randint

tela = tk.Tk()
tela.geometry('600x600+700+230')

def mover():
    
    canvas.move(bola, randint(-10,10) * 0.1, randint(-10,10) * 0.1)
    canvas.move(bola1,randint(-10,10) * 0.1, randint(-10,10) * 0.1)
    canvas.move(bola2,randint(-10,10) * 0.1, randint(-10,10) * 0.1)
    canvas.move(bola3,randint(-10,10) * 0.1, randint(-10,10) * 0.1)
    canvas.move(bola4,randint(-10,10) * 0.1, randint(-10,10) * 0.1)
    canvas.move(bola5,randint(-10,10) * 0.1, randint(-10,10) * 0.1)
    canvas.move(bola6,randint(-10,10) * 0.1, randint(-10,10) * 0.1)
    canvas.after(1, mover)

canvas = tk.Canvas(tela, bg="#5ca5ed")
canvas.pack(fill='both', expand=1, anchor="center")
bola = canvas.create_oval(50, 50,15, 15,  fill="black", width=10, )
bola1 = canvas.create_oval(50, 50,15, 15,  fill="black", width=10, )
bola2 = canvas.create_oval(50, 50,15, 15,  fill="black", width=10, )
bola3 = canvas.create_oval(50, 50,15, 15,  fill="black", width=10, )
bola4= canvas.create_oval(50, 50,15, 15,  fill="black", width=10, )
bola5 = canvas.create_oval(50, 50,15, 15,  fill="black", width=10, )
bola6 = canvas.create_oval(50, 50,15, 15,  fill="black", width=10, )


canvas.after(100, mover)

tela.mainloop()

