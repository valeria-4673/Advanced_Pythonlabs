import tkinter as tk
from random import randint
from tkinter import Button
from tkinter import messagebox
import time

t_inicio = None
def on_off (event):
    global sorted_lista
    global t_inicio

    if t_inicio is None:
        t_inicio = time.time()
    
    clickeando = int(event.widget.cget("text"))
    buscado = sorted_lista [0]
    
    if clickeando == sorted_lista [0]:
            event.widget.config(state=tk.DISABLED)
            sorted_lista.pop(0)
    
    if not sorted_lista:
        t_final = time.time()
        duration = t_final - t_inicio
        bt2.config(text=duration)
    
window = tk.Tk()

lista = []

for i in range(5):
    for j in range(5):
        bt = Button(window, text ="%i" %randint(1, 999))
        anexar = int(bt.cget("text"))
        lista.append(anexar)
        
        bt.grid(row=i, column=j, sticky="nsew")
        bt.bind("<Button-1>", on_off)
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(j, weight=1)
        
print(lista)
sorted_lista = sorted(lista)
print(sorted_lista)

bt2 = Button(window)
bt2.grid(row=5, column=0, columnspan=5, sticky="nsew")

window.mainloop()import tkinter as tk
from random import randint
from tkinter import Button
from tkinter import messagebox
import time

t_inicio = None
def on_off (event):
    global sorted_lista
    global t_inicio

    if t_inicio is None:
        t_inicio = time.time()
    
    clickeando = int(event.widget.cget("text"))
    buscado = sorted_lista [0]
    
    if clickeando == sorted_lista [0]:
            event.widget.config(state=tk.DISABLED)
            sorted_lista.pop(0)
    
    if not sorted_lista:
        t_final = time.time()
        duration = t_final - t_inicio
        bt2.config(text=duration)
    
window = tk.Tk()

lista = []

for i in range(5):
    for j in range(5):
        bt = Button(window, text ="%i" %randint(1, 999))
        anexar = int(bt.cget("text"))
        lista.append(anexar)
        
        bt.grid(row=i, column=j, sticky="nsew")
        bt.bind("<Button-1>", on_off)
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(j, weight=1)
        
print(lista)
sorted_lista = sorted(lista)
print(sorted_lista)

bt2 = Button(window)
bt2.grid(row=5, column=0, columnspan=5, sticky="nsew")

window.mainloop()
