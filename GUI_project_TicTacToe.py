import tkinter as tk
from tkinter import messagebox, Button
import random

wnd = tk.Tk()
wnd.title("TicTacToe")
wnd.geometry("250x250")

disponibles_original = []
disponibles_still = []
gan = [[0 for i in range (3)] for j in range(3)]

def ganador ():
    for i in range(3):
        for j in range(3):
            signal = board[i][j].cget("text")
            if signal == "X":
                signal = 1
                gan[i][j] = signal
            elif signal == "O":
                signal = 2
                gan[i][j] = signal
    print("La lista con 0, 1, 2 numeros es: ", gan)

    for i in range (3):
            if gan[i][0] + gan[i][1] +  gan[i][2] == 3:
                print("Ordenador")
                break
            if gan[i][0] + gan[i][1] +  gan[i][2] == 6:
                print("Ppersona")
                break
    else:
        print("Nadie")
                
    for j in range (3):
            if gan[0][j] + gan[1][j] +  gan[2][j] == 3:
                print("Ordenador")
                break
            if gan[0][j] + gan[1][j] +  gan[2][j] == 6:
                print("Persona")
                break
    else:
        print("Nadie")
        
def cmov_random():
        num_aleatorio = random.randint(0,7)
        tupla_deseada = disponibles_original[num_aleatorio]

        if tupla_deseada in disponibles_still:
            i, j = tupla_deseada
            cmov_1 (board[i][j])
            disponibles_still.remove(tupla_deseada)
        else:
            cmov_random()
            
        
def cmov_1 (bt):
    bt["text"] = "X"
    bt["fg"] = bt["activeforeground"] = "red"

def chum(event):
    bt = event.widget
    quiere = bt.position
    
    if quiere in disponibles_still:
        bt["text"] = "O"
        bt["fg"] = bt["activeforeground"] = "green"
        disponibles_still.remove(quiere)
    else:
        messagebox.showinfo("", "Ocupado")
    cmov_random()
    ganador()
    
board = [["" for i in range (3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        bt = Button(wnd)
        bt.grid(row=i, column=j, sticky="nsew")
        bt.bind("<Button-1>", chum)
        bt.position = (i, j)
        
        if bt.position != (1, 1):
            disponibles_original.append(bt.position)
            disponibles_still.append(bt.position)
            
        wnd.grid_rowconfigure(i, weight=1)
        wnd.grid_columnconfigure(j, weight=1)
        board[i][j] = bt
        
cmov_1(board[1][1])

wnd.mainloop()
