import tkinter as tk
from Frame_Display import DisplayContainer
from Frame_Botoes import ButtonsContainer




root = tk.Tk()
#root.geometry("640x640")
visor = DisplayContainer(root)
numeros = ButtonsContainer(root)







root.mainloop()
