import tkinter as tk
from tkinter import Frame

class Display(Frame):

	def __init__(self , root):
		Frame.__init__(self , root)
		self.criarWidgets()



	def criarWidgets(self):

		self.label_display = tk.Label(self)
		self.label_display["text"] = "0000"
		self.label_display["bg"] = "#bebebe"
		self.label_display["relief"] = "groove"
		self.label_display["bd"] = 5
		self.label_display["height"] = 5
		#self.label_display["width"] = 25
		self.label_display.pack(fill = tk.BOTH)



