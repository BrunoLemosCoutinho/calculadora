import tkinter as tk
from Frame_Display import Display




root = tk.Tk()
root.geometry("800x640")
frame1 = Display(root)
#frame1.grid(row = 0 , column = 0)
frame1.place(x = 15, y = 25)
root.mainloop()
