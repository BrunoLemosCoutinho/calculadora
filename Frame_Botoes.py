import tkinter as tk
from tkinter import Frame

class BotoesAlgarismos(Frame):

	def __init__(self , root):
		Frame.__init__(self , root, borderwidth = 5 , relief = "ridge" )
		self.criarWidgets()




	def criarWidgets(self):

		self.botao = tk.Button(self, text = "oi")
		self.botao.grid(row = 1 , column = 1)
		self.botao2 = tk.Button(self, text = "oi")
		self.botao2.grid(row = 2 , column = 1)
		self.botao3 = tk.Button(self, text = "oi")
		self.botao3.grid(row = 1 , column = 2)
		self.botao4 = tk.Button(self, text = "oi")
		self.botao4.grid(row = 2 , column = 2)

