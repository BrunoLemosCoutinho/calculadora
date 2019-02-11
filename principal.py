import tkinter as tk
from Frame_Display import Display
from Frame_Botoes import BotoesAlgarismos




root = tk.Tk()
#root.geometry("640x640")
visor = Display(root)
numeros = BotoesAlgarismos(root)




visor.grid(row = 1 , column = 1 , columnspan = 2 , ipadx = 100)
numeros.grid(row = 2 , column = 1 , sticky = tk.W + tk.E)



root.mainloop()
