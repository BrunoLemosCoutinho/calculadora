import tkinter as tk
from Frame_Display import DisplayContainer
from Frame_Botoes import ButtonsContainer
from Calculadora import Calculadora


root = tk.Tk()
root.geometry("640x640")
visor = DisplayContainer(root)
numeros = ButtonsContainer(root)
calculadora = Calculadora()
root.mainloop()

