import tkinter as tk
from tkinter import Button

wnd = tk.Tk()
wnd.minsize(width=200, height= 200)

vaso = ""

def dibujar(event):
    global vaso
    bt= event.widget
    num = bt.cget("text")
    if num != "=": 
        vaso += num
    result.set(vaso)
    return vaso

def operar(event):
    escrito = dibujar(event)
    for ch in escrito:
        if ch == "+" or ch== "/":
            spliter = ch           
    operandos = escrito.split(spliter)

    if spliter == "+":
        suma = 0
        for element in operandos:
            suma += int(element)
        print(suma)
        result.set(suma)
        
    if spliter == "/":
        try:
            div = int(operandos[0])/ int(operandos[1])
            result.set(div)
        except ZeroDivisionError:
            result.set("Error")

def clear(event):
    global vaso
    vaso = ""
    result.set("")
    
result = tk.StringVar()
tabler = tk.Label(wnd, textvariable=result, height=2)
tabler.grid(row=0, column=0)

for i in range(8):
    wnd.grid_columnconfigure(i, weight=1)
    
text_buttons = ["0","1","2","3","+","/","=","C"]

for i in range (1, 9):
    bt = Button(wnd, text=text_buttons[i-1])
    bt.bind("<Button-1>", dibujar)
    if i == 7:
        bt = Button(wnd, text=text_buttons[i-1])
        bt.bind("<Button-1>", operar)
    if i == 8:
        bt = Button(wnd, text=text_buttons[i-1])
        bt.bind("<Button-1>", clear)
    bt.grid(row=i, column=0, columnspan=8, sticky="nsew")

wnd.mainloop()
