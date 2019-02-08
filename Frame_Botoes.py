import tkinter as tk
from tkinter import Frame

class BotoesAlgarismos(Frame):

	def __init__(self , root):
		Frame.__init__(self , root,  height = 450 , width = 600, borderwidth = 15 , relief = "ridge" )
		##########self.criarWidgets()




	def criarWidgets(self):

		self.botao = tk.Button(self, text = "oi")
		self.botao.grid(row = 1 , column = 1)
