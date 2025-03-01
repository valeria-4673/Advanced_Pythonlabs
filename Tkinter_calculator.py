import tkinter as tk
from tkinter import messagebox

def operate():
    operando_1 = entry_1.get()
    operando_2 = entry_2.get()
    operador = selected_option.get()
    try:
        if operador == 1:
            resultado= float(operando_1) + float(operando_2)
        else:
            resultado= float(operando_1) - float(operando_2)

        tk.messagebox.showinfo("Resultado",f"{resultado}")
        
    except ValueError:
        tk.messagebox.showinfo("Resultado","Only numbers are acceptable")
        try:
            prueba= float(operando_1)
        except ValueError:
            entry_1.focus()
        try:
            prueba= float(operando_2)
        except ValueError:
            entry_2.focus()
            
wnd = tk.Tk()

entry_1 = tk.Entry(wnd, width= 30)
entry_1.grid(row=2, column=0)

entry_2 = tk.Entry(wnd, width= 30)
entry_2.grid(row=2, column=2)

selected_option = tk.IntVar()

b_suma = tk.Radiobutton(wnd, text="+", variable=selected_option, value=1)
b_suma.grid(row=2, column=1)

b_resta = tk.Radiobutton(wnd, text="-", variable=selected_option, value=2)
b_resta.grid(row=1, column=1)

b_evaluate = tk.Button(wnd, text="Evaluate", command=operate)
b_evaluate.grid(row=3, column=1)

wnd.mainloop()
