import tkinter as tk
from tkinter import Button, Canvas

phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

trabajable = []
for semaforo in phases:
    trabajable.append(list(semaforo))    

current_index = 0

def change_c0():
    canvas.itemconfig(c0, fill='green')

def change_c1():
    canvas.itemconfig(c1, fill='yellow')

def change_c2():
    canvas.itemconfig(c2, fill='red')

def prepare():
    global current_index
    origin()
    if  current_index < len (trabajable):
        sublist = trabajable [current_index]
        
        for bombilla in sublist:    
            if sublist[0] == True:
                change_c0()
            if sublist[1] == True:
                change_c1()
            if sublist[2] == True:
                change_c2()       
        current_index += 1
        
def origin():

    canvas.itemconfig(c0, fill='grey')
    canvas.itemconfig(c1, fill='grey')
    canvas.itemconfig(c2, fill='grey')
    

window = tk.Tk()
window.geometry("350x400")

canvas = tk.Canvas(window, width=300, height=350, bg='grey')

canvas.create_rectangle(75, 0, 225, 320, outline='black',fill='black')
c0 = canvas.create_oval(100, 5, 200, 100, outline='black', width=2, fill='white')
canvas.grid(row=0)
c1 =canvas.create_oval(100, 105, 200, 205, outline='black', width=2, fill='white')
canvas.grid(row=1)
c2 =canvas.create_oval(100, 210, 200, 310, outline='black', width=2, fill='white')
canvas.grid(row=2)

b_next = tk.Button(window, text="Next", command=prepare)
b_next.grid(row=2, column = 1)
b_quit = tk.Button(window, text="Quit", command=window.destroy)
b_quit.grid(row=4)
            
window.mainloop()
