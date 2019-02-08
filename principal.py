import tkinter as tk
from Frame_Display import Display
from Frame_Botoes import BotoesAlgarismos




root = tk.Tk()
root.geometry("800x640")
visor = Display(root)
numeros = BotoesAlgarismos(root)

visor.place( x = 15 , y = 25)
numeros.place( x = 15 , y = 150)
root.mainloop()
