import tkinter as tk
import frame_display
import frame_botoes


root = tk.Tk()
root.geometry("640x640")
visor = frame_display.DisplayContainer(root)
numeros = frame_botoes.ButtonsContainer(root)
root.mainloop()

